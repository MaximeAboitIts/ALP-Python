from datetime import date

AVEC_PRIME = 3

def pourcentage_rabais(annee, nmbAnnee):
    if nmbAnnee >= 5:
        return AVEC_PRIME
    else:
        return 0

def salaireBrut(salaire, pourcentage):
    return salaire * pourcentage / 100 + salaire

def affichage(salaire, salaireFinal, pourcentage, nmbAnnee):
    print("Salaire de base", salaire)
    print("Nombre d'années", nmbAnnee, "ans")
    print("Prime:", pourcentage)
    print("Salaire brut:", salaireFinal)

def main():
    salaire = int(input("Entrez un salaire de base: "))
    annee = int(input("Entrez une année d'engagement: "))
    nmbAnnee = date.today().year - annee

    pourcentage = pourcentage_rabais(annee, nmbAnnee)
    salaireFinal= salaireBrut(salaire, pourcentage)

    affichage(salaire, salaireFinal, pourcentage, nmbAnnee)

main()