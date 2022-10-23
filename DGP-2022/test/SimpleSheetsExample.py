import os
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = '1uNnriEN44iDqDMRunvhAcTXs5wqujoUtz4TJnDRxs1Y'
SAMPLE_RANGE_NAME = 'A1:A11'

key_file_location = os.path.join(os.path.expanduser('~'), 'rasa2022dgp-2ef451d6a1cf.json')
api_key = os.environ['GKEY']
creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, SCOPES)
service = build('sheets', 'v4', credentials=creds, developerKey=api_key)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])