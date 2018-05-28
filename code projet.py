# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:20:25 2018

@author: etudiant
"""
# importation des librairies

import datetime
import time
from datetime import date
# on déclare les variables

xx = int
G = int
reponse_positive = ["oui","ok","o","d'accord","yes","y","ouais"]
reponse_negative = ["non","n","nope","no"]


#------------------------------------------------------------------------------
#
#
#
#
# but:
# avoir un tableau avec chaque traitement = une case
# 1 traitement = [nom, dose, debut, fin]
# resultat : 
# A B C
# 50mg 10mg 1g
# 5/10/18 ... ...
# 8/10/18 ... ...
#
# [["A",50,"5/10/18","8/10/18"],[...]...]
#
#
#
#
#------------------------------------------------------------------------------
#def traitement(nom,dose,debut,duree):
#fin = 0#...
#Tab = [nom,dose,debut,fin]
#return Tab


#def getDate():
#annee = int(input("annee ? "))
#mois = int(input("mois ? "))
#jour = int(input("jour ? "))
# si jour > 0 et <= 31, mois > 0 et <=12, annee > 2000 et < 2500
#return datetime.date(annee,mois,jour)
# sinon return "PB"


#def reponseAffirm(I):
#if I=="oui" or I=="yes" or I=="y" or I=="o" or I=="O":
#return True
#else:
#if I=="non" or I=="no" or I=="n":
#return False
#else:

#return "Poblème"

#------------------------------------------------------------------------------


#
# but :
# avec des print et des input
# recuperer 1 traitement
# et
# le mettre dans la bonne mise en forme
#

#def unSeulTraitement():
#Tab = []
#return Tab



#------------------------------------------------------------------------------
#print(unSeulTraitement())


            

print ("voulez-vous saisir un nouveau traitement ?")
I = input()

if I in reponse_positive: 
    
    G = 1
    while G > 0:  

     print("assignez un nom à votre traitement")
     traitement = input()
        
     print("quel médicament devez-vous prendre ?")
     médicament = input()

     print("quelle est la date du début de votre traitement ? ")
     print("année ?")
     année_début = int(input())
     print("mois ?")
     mois_début = int(input())
     print("jour ?")
     jour_début = int(input())
     début = datetime.date(année_début,mois_début,jour_début)

     print("quelle est la date de fin de votre traitement ?")
     print("année ?")
     année_fin = int(input())
     print("mois ?")
     mois_fin = int(input())
     print("jour ?")
     jour_fin = int(input())
     fin = datetime.date(année_fin,mois_fin,jour_fin)
     if fin <= début:
         print("problème, veuillez ressaisir les informations")
     else:    
    
      print("combien de fois devez-vous prendre votre traitement au cours de la journée ?")
      fréquence = int(input())

      if fréquence == 0 :
          print ("problème, veuillez ressaisir les informations, votre date de fin est située avant votre date de départ")
         
      print("voulez-vous saisir un nouveau traitement ?")
      renouv = input()
      if renouv in reponse_positive:
          G += 1
      if renouv in reponse_negative:
          G = 0
      else:
          print("opération inconnue, veuillez recommencer")
      
      données_du_traitement = [traitement,médicament,année_début,mois_début,jour_début,année_fin,mois_fin,jour_fin,fréquence,début,fin]
      données_traitement = []
      données_traitement += données_du_traitement
         
else:
    if I in reponse_negative:
        print("Opération terminée") 
    else: 
        print("Réponse non reconnue")  

        
if datetime.datetime.now() in range(début,fin) :
    print("prenez votre traitement")
else:
    print("vous n'avez pas de médicament à prendre")        
    
#if xx == fin: