prixInitial = int(input("Veuillez entrer un prix initial: "))
typeVoyageur = int(input("Veuillez entrer le N° du type de voyageur: "))
volEffectue = int(input("Veuillez entrer le nombre de vol effectué: "))
rabais = 0
rabaisSup = 0

if (typeVoyageur == 1):
    rabais = prixInitial * 20 / 100
elif (typeVoyageur == 2):
    rabais = prixInitial * 10 / 100

if (volEffectue == 1):
    rabaisSup = prixInitial * 10 / 100
elif (volEffectue >= 2 and volEffectue <= 4):
    rabaisSup = prixInitial * 15 / 100
elif (volEffectue >= 5):
    rabaisSup = prixInitial * 20 / 100

prixEffectif = prixInitial - rabais - rabaisSup

print("Prix effectif:", prixEffectif)
