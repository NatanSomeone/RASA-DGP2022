from __future__ import print_function

import os.path

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1uNnriEN44iDqDMRunvhAcTXs5wqujoUtz4TJnDRxs1Y'
SAMPLE_RANGE_NAME = 'A1:A11'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    key_file_location = os.path.join(os.path.expanduser('~'), 'rasa2022dgp-2ef451d6a1cf.json')
    api_key = os.environ['GKEY']
    if os.path.exists(key_file_location):
        creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, SCOPES)
    try:
        service = build('sheets', 'v4', credentials=creds, developerKey=api_key)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
