import gspread, random, time
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date

from sheet_control import update_report_cell, err_report

today = "{:%d.%m.%Y}".format(datetime.now())




failed_time = 1
# write current date to google sheet
def alter_update_report_cell(cell_value):
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	emails_sheet = client.open("clreplay").sheet1
	body_text_sheet = client.open("mailbody").sheet1
	replay_links_sheet = client.open("replay_links").sheet1
	try:
		emails_sheet.update_cell(cell_value, 4, today)
	except:
		failed_time += 1
		print (failed_time)
		time.sleep(5)
		update_report_cell(cell_value)


# write user defined error messages to google sheet 
def alter_err_report(cell_value, message):
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by name and open the first sheet
	emails_sheet = client.open("clreplay").sheet1
	body_text_sheet = client.open("mailbody").sheet1
	replay_links_sheet = client.open("replay_links").sheet1
	try:
		emails_sheet.update_cell(cell_value, 5, message)
	except:
		failed_time += 1
		print (failed_time)
		time.sleep(5)
		err_report(cell_value, message)