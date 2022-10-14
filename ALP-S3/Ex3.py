prixUnitaire = int(input("Entrez un prix unitaire: "))
nombrePieces = int(input("Entrez un nombre de pièces: "))
totalAvantRabais = prixUnitaire * nombrePieces

def calcul_prix_a_payer():
    rabais = 0
    if(nombrePieces > 100):
        rabais = totalAvantRabais * 10 / 100

    totalApresRabais = totalAvantRabais - rabais
    afficher_prix_a_payer(totalApresRabais, rabais)

def afficher_prix_a_payer(total, rabais):
    print("Pour", nombrePieces, "pièces à", prixUnitaire, ":")
    print("Prix avant rabais:", totalAvantRabais)
    print("Montant du rabais:", rabais)
    print("Prix à payer:", total)

calcul_prix_a_payer()