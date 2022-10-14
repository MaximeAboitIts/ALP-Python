from datetime import date

age = int(input("Entrez l'âge du spectateur: "))
nmbTarif = int(input("Entrez un numéro de tarif: "))
jour = date.today().weekday()
prix = 0
reduction = 0

if (age <= 7):
    prix = 5
elif (age <= 18):
    prix = 10
else:
    prix = 15

if (jour == 0 and nmbTarif == 1):
    reduction = prix * 20 / 100
elif (jour == 1 and nmbTarif == 2):
    reduction = prix * 10 / 100
elif (jour == 3 and nmbTarif == 2):
    reduction = prix * 10 / 100

prixFinal = prix - reduction

print("Prix à payer:", prixFinal)
