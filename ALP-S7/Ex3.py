def calcul_capital(capital, interet, nmb_periode):
    for i in range(nmb_periode):
        capital += capital * interet / 100
    return capital

def affichage(capital, interet, nmb_periode):
    print(f"Le capital obtenu est de {calcul_capital(capital, interet, nmb_periode)}")

def main():
    capital = float(input("Entrez un capital de départ : "))
    interet = float(input("Entrez un taux d'intérêt : "))
    nmb_periode = int(input("Entrez un nombre de périodes : "))

    affichage(capital, interet, nmb_periode)

main()