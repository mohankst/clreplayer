import gspread, random, pyperclip, time, pyautogui
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#importing local files
from sheet_control import get_data, rand_re_link, get_body_text
from mail_login import login_gmail

#geeting todays date as string
today = "{:%d.%m.%Y}".format(datetime.now())
#defining the cell to marking for job done
cell_value = 1

links = rand_re_link()
body_text = get_body_text()

for row in get_data():
	email = row['Email']
	password = row['Password']
	remail = row['Recovery']
	reporting_date = row['Reporting Date']
	cell_value += 1

	if reporting_date == today:
		continue
	#defining webdriver instance
	driver = webdriver.Chrome()
	#driver = webdriver.Firefox(executable_path='geckodriver.exe')

	login_gmail(driver, email, password, remail, cell_value)
	if login_gmail == False:
		driver.quit()
		continue

	# sending email for 25 times
	for _ in range(25):
		time.sleep(5)
		replay_link = random.choice(links)
		driver.get("{}".format(replay_link))
		wait = WebDriverWait(driver, 120)
		mailbody_imput = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":nn"]')))
		mailbody_imput.click()
		rand_body_text = random.choice(body_text)
		mailbody_imput.send_keys(Keys.UP * 2)
		mailbody_imput.send_keys(rand_body_text)
		mailbody_imput.send_keys(Keys.CONTROL + "v")
		mail_send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":p0"]')))
		mail_send_button.click()
		time.sleep(3)


	# close the webdriver instance
	driver.quit()
