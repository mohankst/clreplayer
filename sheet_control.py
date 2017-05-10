import gspread, random, time
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
emails_heet = client.open("clreplay").sheet1
body_text_sheet = client.open("mailbody").sheet1


mailbody = body_text_sheet.get_all_records()

body_text_sheet = client.open("mailbody").sheet1
mailbody = body_text_sheet.get_all_records()

def get_data():
	data = emails_heet.get_all_records()
	return data

get_data()