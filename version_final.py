# -*- coding: utf8 -*-
# coding : utf8

import time
import gspread
import os
import sys
import time
import datetime
import speech_recognition as sr
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


def list_microphones():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))
        
    print("\n\n")

def get_vocal_command():

	r = sr.Recognizer()

        with sr.Microphone(device_index=1) as source:
  		r.adjust_for_ambient_noise(source, duration = 1)
                r.energy_threshold =1000
                print("Say something !")
                              
                audio = r.listen(source,None,2)
                print("Trying to recognize audio")

                try:
                        t=r.recognize_google(audio, language='fr_FR')
                        print ("You just said : " +t)               
                                   
                except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")

                except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))



while 1:

	for i in range(0,len(time_totale_date)):
		
		if time.strftime("%H:%M",time.localtime()) == time_totale_date[i]:
			if  time.strftime("%H:%M",time.localtime())=='07:45' or time.strftime("%H:%M",time.localtime())=='07:00' :
				tts0=gTTS(" Bonne  matinée vous avez des medicament a prendre Aujourdhuit je vous souhaite une bonne journee" ,lang="fr")
				tts0.save('medica0.mp3')
				os.system("mpg123 medica0.mp3")
				time.sleep(50)
		 		

							
			
			time_heure=time.strftime("%H:%M",time.localtime())
			if time.strftime("%H:%M",time.localtime()) == time_totale_heure[i]:
			
				indice1=time_totale_heure.index(time_heure)
				print(indice1)		
			
				medicament=sheet.cell(indice1+1,3).value
				mode_prise=sheet.cell(indice1+1,5).value
				quantite=sheet.cell(indice1+1,4).value	
				  		
				tts1=gTTS("c est " + time_heure + " vous deverez prendre " + quantite + " du medicament " + medicament ,lang="fr")
				tts1.save('medica1.mp3')
				tts2=gTTS("De la maniere suivante "+mode_prise, lang="fr")
				tts2.save('medica2.mp3')
				
				os.system("mpg123 medica1.mp3")
				time.sleep(1)
				os.system("mpg123 medica2.mp3")
				list_microphones()
				a=get_vocal_command()
				if a=='ok':
					
					sheet.update_cell(inice1+1, 6, " le médicament est pris par le patient ")
					time.sleep(45)
				else:
					sheet.update_cell(indice1+1, 6, "le médicament n'est pris par le patient")
					time.sleep(45)
				break
