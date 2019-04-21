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
info = [
    ["'1-3 Star Ema List'!D3:G", "Hitagi Crab"],
    ["'1-3 Star Ema List'!J3:M", "Mayoi Snail"],
    ["'1-3 Star Ema List'!P3:S", "Suruga Monkey"],
    ["'1-3 Star Ema List'!V3:Y", "Nadeko Snake"],
    ["'1-3 Star Ema List'!AB3:AE", "Tsubasa Cat"],
    ["'1-3 Star Ema List'!AH3:AK", "Karen Bee"],
    ["'1-3 Star Ema List'!AT3:AW", "Zaregoto"]
]

def updateDB():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()

    f = open("emaList.json", "w")

    f.write("{\n")
    f.write('"data" : [\n')

    for inf in info:
        result = sheet.values().get(spreadsheetId=spreadsheet,
                                    range=inf[0]).execute()
        values = result.get('values', [])
        l = len(values)

        if not values:
            print('No data found.')
        else:
            for i in range(0, l):
                howto = values[i][0].replace('\n', " ")

                f.write('\t\t[ "%s", "%s", "%s", "%s", "%s" ]' % (howto, values[i][1], values[i][2], values[i][3], inf[1]))

                if (inf[1] != "Kubikiri Cycle Zaregoto" or i<l-1):
                    f.write(",\n")

    f.write("\t]\n")
    f.write("}")
    f.close()

def loadDB():
    f = open("emaList.json")
    jfile = json.load(f)
    db = dict()
    for arc in info:
        db[arc[1]]=[]
    for ema in jfile["data"]:
        db[ema[4]].append(ema)
    return db

if __name__ == '__main__':
    x = loadDB()
    print(x["Hitagi Crab"])
