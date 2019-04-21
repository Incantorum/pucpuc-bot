from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os
import json

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

spreadsheet = '1swb1SG-A9t9xxdfXTQprCGmzICDISK4QASL_dX9J5sY'

#tabs to translate and its range
info = [
    "'Intro'!A:H",
    "'Puc Skills'!A:N",
    "'4-5 Star Ema Skills'!A:N",
    "'1-3 Star Ema Guide'!C1:C30",
    "'Top Tier Strats (Translated ver.)'!A:I"
]

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))
sheet = service.spreadsheets()

for s_range in info:        
    result = sheet.values().get(spreadsheetId=spreadsheet,range=s_range).execute()
    values = result.get('values', [])

    mode = 2

    if mode == 1:
        for i in range(0,len(values)):
            for j in range(0,len(values[i])):
                if(values[i][j]!="" or ("GOOGLETRANSLATE" in values[i][j]) ):
                    values[i][j] = '=GOOGLETRANSLATE("%s", "en", "es")' % values[i][j]
    elif mode == 0:
        for i in range(0,len(values)):
            for j in range(0,len(values[i])):
                if(values[i][j]!="" or ("GOOGLETRANSLATE" in values[i][j]) ):
                    cad = values[i][j].split('"')
                    print (cad)
                    values[i][j] = cad
    elif mode == 2:
        for i in range(0,len(values)):
            for j in range(0,len(values[i])):
                if("Tamaño Hasta" in values[i][j]):
                    values[i][j] = values[i][j].replace("Tamaño Hasta", "Aumento")
                if("Tamaño Up" in values[i][j]):
                    values[i][j] = values[i][j].replace("Tamaño Up", "Aumento")
                if("gama" in values[i][j]):
                    values[i][j] = values[i][j].replace("gama", "Rango")
                if("Coste" in values[i][j]):
                    values[i][j] = values[i][j].replace("Coste", "Costo")
                if("Tamaño de Hasta" in values[i][j]):
                    values[i][j] = values[i][j].replace("Tamaño de Hasta", "Aumento")
                if("Habilidad Calibrador" in values[i][j]):
                    values[i][j] = values[i][j].replace("Habilidad Calibrador", "Indicador")
    body = {
        'values': values
    }

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet, range=s_range,
        valueInputOption="USER_ENTERED", body=body).execute()