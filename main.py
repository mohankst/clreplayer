import gspread
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("clreplay").sheet1

# Extract and print all of the values
data = sheet.get_all_records()

#geeting todays date as string
today = "{:%d.%m.%Y}".format(datetime.now())

#defining the cell to marking for job done
cell_value = 1

for row in data:
	email = row['Email']
	password = row['Password']
	remail = row['Recovery']
	cell_value += 1
	sheet.update_cell(cell_value, 5, today)
	sheet.update_cell(cell_value, 6, "Problem")
	print ('{0} {1}'.format (email, password))
