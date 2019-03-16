# -*- coding: utf8 -*-
# coding : utf8

import time
import gspread
import os
import sys
import time

from gtts import gTTS
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ListMedicament.json',scope)

client = gspread.authorize(creds)
sheet = client.open("ListMedicament").sheet1

time_totale_heure=sheet.col_values(2)
time_totale_date=sheet.col_values(1)

time_date=time.strftime("%d/%m/%Y",time.localtime())
time_heure=time.strftime("%H:%M",time.localtime())
medicament=sheet.cell(2,3).value
mode_prise=sheet.cell(2,4).value

tts0=gTTS(" vous devez prendre le medicament "+ medicament  " ,lang="fr")
tts1=gTTS(" De la manière suivante "+ mode_prise  " ,lang="fr")         
tts0.save('medica0.mp3')
tts1.save('medica1.mp3')
os.system("mpg123 medica0.mp3")
          

