import gspread, random, time
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date

from alter_sheet_control import alter_update_report_cell, alter_err_report, alter_rand_re_link

today = "{:%d.%m.%Y}".format(datetime.now())

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
emails_sheet = client.open("clreplay").sheet1
body_text_sheet = client.open("mailbody").sheet1
replay_links_sheet = client.open("replay_links").sheet1


mailbody = body_text_sheet.get_all_records()

body_text_sheet = client.open("mailbody").sheet1
mailbody = body_text_sheet.get_all_records()

#geeting all email informaitons 
def get_data():
	data = emails_sheet.get_all_records()
	return data


#geeting body text for emails
def get_body_text():
	amb = [] #defining an empty list for all mailbody
	mailbody = body_text_sheet.get_all_records()
	for row in mailbody:
		bt = row['texts']
		amb.append(bt)
	random.shuffle(amb)
	body_text = random.choice(amb)
	return body_text


# write current date to google sheet
def update_report_cell(cell_value):
	try:
		emails_sheet.update_cell(cell_value, 4, today)
	except:
		time.sleep(5)
		alter_update_report_cell(cell_value)

# write user defined error messages to google sheet 
def err_report(cell_value, message):
	try:
		emails_sheet.update_cell(cell_value, 5, message)
	except:
		time.sleep(5)
		alter_err_report(cell_value, message)

#geeting replay links randomly from google sheet
def rand_re_link():
	links = []
	try:
		data = replay_links_sheet.get_all_records()
	except:
		alter_rand_re_link()
	for row in data:
		replay_link = row['links']
		links.append(replay_link)
	random.shuffle(links)
	re_link = random.choice(links)
	return re_link

