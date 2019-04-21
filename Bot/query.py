from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import json

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
spreadsheet = '1JVWv1nTdpagMDC5cEExYvQmiluBnpkx4Y1Kypl74bIk'

#Ranges of each state and the name of the file
info = ["'Puc Skills'!B2:M42", "INSERT_PUC.sql"]

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    result = sheet.values().get(spreadsheetId=spreadsheet,
                                range=info[0]).execute()
    values = result.get('values', [])

    f = open(info[1], "w")

    if not values:
        print('No data found.')
    else:
        for val in values:
            if(val[10]!=""): score = int(val[10])
            else: score = 0
            f.write("INSERT INTO puc (puc_name, puc_tier, puc_scoreAt100, puc_OST) VALUES('%s', '%s', %s, '%s');\nGO\n\n" % (val[0], val[2], score, val[11]))

if __name__ == '__main__':
    main()