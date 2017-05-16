from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#importing local files
from sheet_control import update_report_cell, rand_re_link




def login_gmail(driver, email, password, remail, cell_value):
	mail_problem = False
	replay_link = random.choice(rand_re_link())
	driver.get("{}".format(replay_link))
	# driver.get("https://mail.google.com")
	wait = WebDriverWait(driver, 10)
	try:
		gmail_signin_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > nav > div > a.gmail-nav__nav-link.gmail-nav__nav-link__sign-in')))
		gmail_signin_btn.click()
	except:
		pass
	try:
		gmail_user_id_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierId"]')))
	except:
		gmail_user_id_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="Email"]')))
	gmail_user_id_field.click()
	gmail_user_id_field.send_keys(email)
	gmail_user_id_field.send_keys(Keys.RETURN)
	gmail_password_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
	gmail_password_field.send_keys(password)
	gmail_password_field.send_keys(Keys.RETURN)
	try:
		remail_field = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[1]/div/div[2]')))
		remail_field.click()
		remail_field_imput = wait.until(EC.element_to_be_clickable((By.ID, 'knowledge-preregistered-email-response')))
		remail_field_imput.send_keys(remail)
		remail_field_imput.send_keys(Keys.RETURN)
	except:
		pass
	# Print reporting date to google sheet after log in
	update_report_cell(cell_value)

	try:
		wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()[contains(.,"Account disabled")]]')))
		message = "Problem (Account disabled)"
		err_report(cell_value, message)
		driver.quit()
		mail_problem = True
	except:
		pass
	return mail_problem