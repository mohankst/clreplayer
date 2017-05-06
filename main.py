import gspread
from datetime import datetime, date
from oauth2client.service_account import ServiceAccountCredentials

#geeting todays date as string
today = "{:%d.%m.%Y}".format(datetime.now())


#Geeting mailbody text from file


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("clreplay").sheet1

# Find a workbook by name and open the 2nd sheet
body_text_sheet = client.open("mailbody").sheet1
mailbody = body_text_sheet.get_all_records()

#get random mailbody
def load_mailbody(mb=mailbody):
	amb = [] #defining an empty list for all mailbody
	for text in mb:
		amb.append(text)
	random.shuffle(amb)
	return amb
body_text = load_mailbody()

# Extract all of the values
data = sheet.get_all_records()

#defining the cell to marking for job done
cell_value = 1

for row in data:
	email = row['Email']
	password = row['Password']
	remail = row['Recovery']
	cell_value += 1
	sheet.update_cell(cell_value, 4, today)
	sheet.update_cell(cell_value, 5, "Problem")
	print ('{0} {1}'.format (email, password))
