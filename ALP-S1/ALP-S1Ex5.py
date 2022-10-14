prixUnitaire = int(input("Veuillez entrer le prix unitaire: "))
nmbPieces = int(input("Veuillez entrer le nombre de pièces: "))
prixAvantRabais = prixUnitaire * nmbPieces
rabais = 0

if(nmbPieces > 100):
    rabais = prixAvantRabais * 10/100

prixApresRabais = prixAvantRabais - rabais

print("Pour", nmbPieces, "pièces à", prixUnitaire, ":")
print("Prix avant rabais:", prixAvantRabais)
print("Montant du rabais:", rabais)
print("Prix à payer:", prixApresRabais)