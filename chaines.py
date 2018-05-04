#!/usr/bin/env python
# encoding : utf-8


#################################################################################################
#   _                _         _                  _                           _   __            #
#  | |   ___ ___  __| |_  __ _(_)_ _  ___ ___  __| |___   __ __ _ _ _ __ _ __| |_ \_\ _ _ ___   #
#  | |__/ -_|_-< / _| ' \/ _` | | ' \/ -_|_-< / _` / -_) / _/ _` | '_/ _` / _|  _/ -_) '_/ -_)  #
#  |____\___/__/ \__|_||_\__,_|_|_||_\___/__/ \__,_\___| \__\__,_|_| \__,_\__|\__\___|_| \___|  #
#                                                                                               #
#################################################################################################

# Le but final de cette activit� est d'�crire petit programme de cryptographie qui permet de chiffrer et d�chiffrer des messages en utilisant le chiffrement de C�sar. On devrait au final arriver notamment � d�chiffrer des messages comme ceux-ci :

message_secret1 = 'mhvxlvmxohvfhvdu'
message_secret2 = 'dwwdtxhdodxeh'
message_secret3 = "M�spjp{h{pvuz'(']v|z'�{lz'hyyp}�z'�'k�jopmmyly'jl'tlzzhnl5'Sl'jvkl'kl'J�zhy'u.h'k�zvythpz'ws|z'kl'zljyl{z'wv|y'}v|z5"

# Chemin faisant, nous prendrons aussi l'occasion pour voir (ou revoir) comment on manipule du texte en informatique (et plus particuli�rement en Python) !

# En informatique, une cha�ne de caract�re (string en anglais) est le type qui permet la manipulation du texte par un programme. Une cha�ne de caract�re est tout simplement une s�quence de symboles (lettres, espaces, saut de lignes, caract�res de ponctuations, symb�les divers). En somme, du texte brut (sans formattage) comme on en trouverait dans un fichier txt. Passons en revue quelques fonctionnalit�s de bases des chaines de caract�res.

######################
# d�finir une chaine #
######################
# Pour d�finir une chaine de caract�re dans Python, on peut taper une s�quence de symboles d�limit�e au d�but et � la fin par des accolades ', des  guillements ", ou des triples guillemets """ :

ma_chaine1 = 'Je ne saute pas '
ma_chaine2 = "de ligne !"
ma_chaine3 = """Un texte mis entre triples guillemets peut contenir des
sauts
de lignes."""

# On peut ne rien mettre entre les symboles d'ouverture et fermeture, on cr�e alors une chaine vide :

chaine_vide = '' # une chaine de caract�re qui ne contient aucun caract�re !

#########
# print #
#########
# La fonction print permet d'afficher une chaine de caract�re. Notez que la fonction passe � la ligne � chaque appel :

print("Deux appels successifs de la fonction print :")
print(ma_chaine1) # saut de ligne
print(ma_chaine2)

#################
# concat�nation #
#################
# Sur les chaines de caract�res, on dispose d'un op�rateur de concat�nation, not� par le symbole +, qui cr�e une cha�ne compos�e des deux chaines accol�es � la suite :

print("Avec concat�nation :")
print(ma_chaine1 + ma_chaine2)

################################
# multiplication par un entier #
################################
# On peut multiplier une chaine de caract�res par un entier pour la r�p�ter plusieurs fois :

print("All work and no play makes Jack a dull boy.\n" * 10)

#########
# input #
#########
# la fonction input permet de demander � l'utilisateur de saisir une chaine de caract�res. Le programme attend alors que l'utilisateur tape du texte au clavier. L'�xecution du programme reprend d�s que l'utilisateur appuie sur la touche entr�e :

ma_chaine4 = input("Veuillez saisir du texte : ")
print("Tu as tap� : " + ma_chaine4)


#######
# str #
#######
# On peut convertir une variable en une chaine de caract�re � l'aide de la fonction str :

quarante_deux = str(42) # '42'

print("la r�ponse est " + quarante_deux)



print(
"""
######################################
# Parcourir une chaine de caract�res #
######################################
"""
)
# On peut manipuler une chaine de caract�res de mani�re assez similaire � un tableau. Par exemple, on peut acc�der � une partie d'une chaine de cart�res comme pour un tableau � l'aide de la syntaxe chaine[i] :

chaine = "Bonjour !"

print(chaine[0])    # B
print(chaine[:3])   # Bon
print(chaine[3:])   # jour !
print(chaine[4:6])  # ou
print(chaine[-1])   # !

#######
# len #
#######
# Comme pour les tableaux, la fonction len() retourne la longueur d'une chaine.

print(len("chaine de caract�res")) # 20

# L'utilisation de la fonction len() permet notamment le parcours d'une chaine de caract�re comme une liste. Selon vous, que fait le code de la fonction suivante ?

def fonction(chaine):
    compteur = 1
    for i in range(len(chaine)):
        if chaine[i] == ' ':
            compteur += 1
    return compteur
    
# Vous pouvez tester votre hypoth�se en utilisant la fonction sur des exemples :
print("test de la fonction :")
nombre = fonction("ma super chaine")
print(nombre)

# La boucle for peut �galement parcourir directement les �l�ments de la chaine, sans utiliser les indices : 

for caractere in chaine :
    # on fait des choses
    pass
    
def fonction(chaine):
    compteur = 1
    for caractere in chaine:
        if caractere == ' ':
            compteur += 1
    return compteur

##### 
# 1 #
#####

# Niveau 1 : � l'aide d'une boucle for, programmer une fonction compter_occurences(caractere, chaine) qui retourne le nombre d'occurence du caract�re c dans la cha�ne s


def compter_occurences(caractere, chaine):
    # retourne le nombre d'occurences du caract�re dans la chaine
    
    pass # remplacer cette ligne par votre code
 
# quelques tests : 
# assert compter_occurences('o', 'bonjour') == 2
# s = "En ce mement, certes, t�es le chef, mets � beleve me � ce temps est bref et je prefere etre dens mes semelles qe dens tes empegnes !"
# assert compter_occurences('e', s) == 35
# assert compter_occurences('a', s) == 0



##### 
# 2 #
#####

# Niveau 1 : En utilisant votre fonction compter_occurence, programmer une fonction compter_mots(chaine) qui retourne le nombre de mot dans la chaine. On suppose ici qu'un mot est simplement une sequence de symbole sans espace (il s'agit d'un mod�le tr�s simpliste, mais on s'en contentera). La fonction doit retourner 0 pour une chaine vide.

def compter_mots(chaine):
    # retourne le nombres de mot dans la chaine
    
    pass # remplacer cette ligne par votre code
    
# quelques tests :
# assert compter_mots("") == 0
# assert compter_mots("anticonstitutionnellement") == 1
# assert compter_mots("Ceci est un chaine de caract�res qui contient dix mots.") == 10
    
##### 
# 3 #
#####

# Niveau 2 : Toujours � l'aide d'une boucle for programmer une fonction compter_occurences(mot, chaine) qui retourne le nombre d'occurence du mot dans la chaine

def compter_occurences_mot(mot, chaine):
    # retourne le nombre d'occurence de mot dans la chaine
    
    pass # remplacer cette ligne par votre code
    

# quelques tests
# assert compter_occurences_mot('bla', 'blablabla') == 3
# assert compter_occurences_mot('haha', 'hahaha') == 2



#####################################
# Modifier une chaine de caract�res #
#####################################

# Contrairement � un tableau, il n'est pas possible de modifier la valeur d'un caract�re dans une chaine par affectation (on dit qu'une chaine de caract�re est immuable). Par exemple, le code suivant provoque une erreur :

chaine = "adieux canard !"
try :
    chaine[0] = 'o' # va provoquer une TypeError
except TypeError:
    print("Une cha�ne de caract�res est un objet immuable en Python.")
    
# Pour contourner cette limitation, il peut �tre utile de transformer une chaine en une liste de caract�res � l'aide de la fonction list(). On peut ensuite effectuer l'op�ration inverse en utilisant ''.join(). Par exemple d'effectuer cette op�ration (techniquement, on ne modifie pas la cha�ne s originale, on la remplace en int�gralit� par une nouvelle cha�ne): 

liste = list(chaine) # on transforme s en list
liste[0] = 'o' # on change le premier �l�ment de la liste
chaine = ''.join(liste) # on retransforme la liste l en une cha�ne
print(chaine)

##### 
# 4 #
#####

# Niveau 1 : En utilisant list et join, programmer une fonction substituer() qui retourne une chaine o� l'on a mis un certain caract�re en position i.

def modifier(chaine, caractere, i):
    # retourne la chaine dans laquelle le caract�re en position i a �t� modifi� pour devenir caractere
    
    pass # remplacer cette ligne par votre code

# tests
# assert modifier("balle", "u", 1) == "bulle"
# assert modifier("adieux canard !", "o", 0) == "odieux canard !"

##### 
# 5 #
#####

# Niveau 2 : Programmer une fonction substituer_mot qui remplace toutes les occurences d'un mot par un autre mot. On pourra utiliser les m�thodes split et join. Attention : si le mot de remplacement est vide, on veut en fait supprimer les occurences de mot original.
    
def substituer(chaine, mot, remplacement):
    # retourne la chaine o� toutes les occurences de mot ont �t� remplac�es par remplacement
    
    pass # remplacer cette ligne par votre code

# quelques tests
# assert substituer("l'homme est un loup pour l'homme", "l'homme", "le loup") == "le loup est un loup pour le loup"
# assert substituer('Interdiction de prononcer le mot tabou qui est d�sormais tabou !', 'tabou', '') == 'Interdiction de prononcer le mot qui est d�sormais !' # attention aux �ventuels doubles espaces...


##### 
# 6 #
#####

# Optionnel : � partir de votre fonction substituer, impl�menter : https://www.xkcd.com/1288/
# c'est-�-dire programmer une fonction xkcd qui prend en argument une chaine et un dictionnaire de substititions � effectuer, et qui retourne la chaine o� toutes les substitutions ont �t� effectu�e.


def xkcd(chaine, substitutions):
    # impl�matation de https://www.xkcd.com/1288/
    # la fonction prend en argument une chaine et un dictionnaire de substititions � effectuer, et retourne la chaine o� toutes les substitutions ont �t� effectu�e.
    
    pass # remplacer cette ligne par votre code


##########################
# La table ASCII/Unicode #
##########################
 
# Pour encoder une chaine de caract�re dans la m�moire de l'ordinateur, il faut attribuer � chaque caract�re un num�ro (qui est stock� en binaire dans la m�moire). Le choix est a priori aribtraire (et il a exist� plusieurs standards d'encodages diff�rents), mais deux standards sont tr�s r�pandus et sont utilis� dans Python : ASCII et Unicode. La table ASCII (American Standard Code for Information Interchange), est une des premi�res tables de ce genre (sa cr�ation remonte aux ann�es 60) et la plus universellement utilis�e. Mais elle �tait con�ue pour l'anglais et ne contient aucun caract�re accentu�, ou autres alphabets. La table Unicode est une extension de la table ASCII qui contient tous ces caract�res manquant, et est devenu aujourd'hui le standard dominant.

# En python, pour obtenir le num�ro d'un caract�re, on utilise la fonction ord()

print(ord('a')) # 97

# Et r�ciproquement, pour obtenir un caract�re � partir de son num�ro, on utilise la fonction chr()

print(chr(97)) # a

##### 
# 7 #
#####

# Niveau 1 : � partir des fonctions ord et chr, �crire une fonction decaler(caractere, decalage) qui permet de trouver le caract�re un certain nombre de rangs plus loin dans la table ASCII/Unicode

def decaler(caractere, decalage):
    # retourne le caract�re qui se trouve un certain nombre de rangs plus loin dans la table ASCII/Unicode (le nombre est donne par l'entier decalage)
    
    pass # remplacer cette ligne par votre code

##### 
# 8 #
#####

# Niveau 2 : En utilisant votre fonction decaler, programmer une fonction chiffrement_cesar qui prend en argument un message (chaine de caract�re), et une cl� (entier), et retourne le message chiffr� par le chiffre de C�sar avec le cl�.

  
def cesar(message, cle):
    # retourne le message chiffr� par le code de C�sar avec la cl�
    
    pass # remplacer cette ligne par votre code

# tests
# assert cesar('bonjour', 1) == 'cpokpvs'
# assert cesar('JulesCesar', 3) == 'MxohvFhvdu'
# assert cesar('glevefme', -4) == 'charabia'

# Niveau 2 : En utilisant votre fonction chiffrement_cesar, programmer une fonction dechiffrement_cesar qui effectue l'op�ration inverse

def dechiffrement_cesar(message_chiffre, cle):
    # retourne le message d�chiffr� par le code de C�sar avec la cl�
    
    pass # remplacer cette ligne par votre code


# tests
# assert dechiffrement_cesar('cpokpvs', 1) == 'bonjour'
# assert dechiffrement_cesar('MxohvFhvdu', 3) == 'JulesCesar'

#####
# 9 #
#####

# Niveau 3 : Comment trouver la cl� d'un message chiffr� par le code de c�sar ? Utilisez cette m�thode pour d�chiffrer les messages contenus dans les variables message_secret1, message_secret2 et message_secret3

