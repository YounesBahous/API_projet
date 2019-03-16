import gspread 
import os
import time 
from gtts import gTTS
from oauth2client.service_account import ServiceAccountCredentials

creds = ServiceAccountCredentials.from_json_keyfile_name('ListMedicament.json',scope)

client = gspread.authorize(creds)
sheet = client.open("ListMedicament").sheet1


time_totale=sheet.col_values(1)

time_now=time.strftime("'u'%m/%d %H:%M",time.localtime())

print(time_now)

for i in range(0,len(time_totale)):

    if time_now in time_totale:

        indice=time_totale.index(time_now)
        medicament=sheet.cell(indice, 2).value
        mode_prise=sheet.cell(indice, 3).value
        
        print(medicament)
        break
        print(medicament)
        break


import time
import gspread
import os
from gtts import gTTS
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ListMedicament.json',scope)

client = gspread.authorize(creds)
sheet = client.open("ListMedicament").sheet1


time_totale=sheet.col_values(1)

time_now=time.strftime("'u'%m/%d %H:%M",time.localtime())
 
print(time_now)
for i in range(0,len(time_totale)):

    if time_now in time_totale:
		
	indice=time_totale.index(time_now)
	medicament=sheet.cell(indice, 2).value
	mode_prise=sheet.cell(1, 3).value	
  	tts1=gTTS("vous deverez prend  " + medicament ,lang="fr")
	
	time.sleep(2)

	tts2=gTTS("De la maniére suivant " + mode_prise , lang="fr")
	with open('from_file.mp3', 'wb') as fp:
   	 	tts1.write_to_fp(fp)
    		tts2.write_to_fp(fp)
        os.system("from_file.mp3")
     else:
	print("aucun médicament à prendre")









tts = gTTS("SETI")
tts.save("SETI.mp3")
os.system("mpg321 SETI.mp3")
