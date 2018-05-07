# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:20:25 2018

@author: etudiant
"""

import datetime

print("assignez un nom à votre traitement")
traitement = input()

print("quel médicament devez-vous prendre ?")
medicament = input()

print("quelle est la date du début de votre traitement ? ")
print("année ?")
x = int(input())
année = x
print("mois ?")
y = int(input())
mois = y
print("jour ?")
z = int(input())
jours = z
début = datetime.date(x,y,z)

print("quelle est la date de fin de votre traitement ?")
print("année ?")
a = int(input())
année = a
print("mois ?")
b = int(input())
mois = b
print("jour ?")
c = int(input())
jours = c
fin = datetime.date(a,b,c)

print("combien de fois devez-vous prendre votre traitement au cours de la journée ?")



