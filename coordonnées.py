print("créez un compte")

print("entrez votre nom") 
nom = input()

print("entrez votre prénom")
prenom = input()

print("entrez votre âge")
age = int(input())

print("entrez votre adresse")
adresse = input()

print("entrez votre adresse mail")
mail = input()

print("entrez votre numéro de téléphone")
téléphone = int(input())

print("votre compte a été créé avec succès")



f = open("moncompte.txt",'w')
f.write("nom : "+str(nom) + "\n")
f.write("prenom : "+str(prenom) + "\n")
f.write("age : "+str(age) + "\n")
f.write("adresse : "+str(adresse) + "\n")
f.write("mail : "+str(mail) + "\n")
f.write("téléphone : "+str(téléphone) + "\n")


f.close()