from datetime import date

salaireDeBase = int(input("Veuillez entrer le salaire de base: "))
anneeEngagement = int(input("Veuillez entrer l'année d'engagement: "))
nmbAnnee = date.today().year - anneeEngagement
prime = 0

if (nmbAnnee >= 5 and nmbAnnee <= 10):
    prime = salaireDeBase * 3 / 100
elif (nmbAnnee > 10):
    prime = salaireDeBase * 7 / 100

salaireBrut = salaireDeBase + prime

print("Salaire de base:", salaireDeBase)
print("Nombre d'année d'engagement:", nmbAnnee, "ans")
print("Prime:", prime)
print("Salaire brut:", salaireBrut)
