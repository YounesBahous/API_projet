#a=['a','d','e','c','r','t']
#variable= input("entrer une chaine")
#if variable in a:
   # print("elle est presente")
#else:
    #print("non presente")

# -*- coding: utf8 -*-
# coding : utf8 

def comparaison(a1,a2):
        if a1==a2:
            print("aucun gangant égalité")

        elif ((a1 == "ciseau" and a2 =="pierre") or (a1 == "papier" and a2 =="ciseau") or (a1 == "pierre" and a2 =="papier")):
			print("%s est le gagnant " , joueur2)
		else :
			print("%s est le gagnant ", joueur1)
        
joueur1=input (" quel est votre nom pour joueur 1: ")
joueur1_answer=input("%s quel est votre choix:"%joueur1)

joueur2=input (" quelle est votre nom pour joueur 2: ")
joueur2_answer=input("%s quel est votre choix:"%joueur2)   

comparaison(joueur1_answer,joueur2_answer)





          



