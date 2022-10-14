# Imports

# Constantes
rabais_50_piece = 3
rabais_100_piece = 5
rabais_1000_piece = 10

tva_250_piece = 8.2
tva_500_piece = 6.3
tva_plus_500_piece = 4.5
# Procédures et fonctions
def calcul_rabais(nombre_piece):
    if(nombre_piece >= 50 and nombre_piece <= 99):
        return rabais_50_piece
    elif(nombre_piece >= 100 and nombre_piece <= 999):
        return rabais_100_piece
    elif(nombre_piece >= 1000):
        return rabais_1000_piece
    else:
        return 0

def calcul_tva(nombre_piece):
    if(nombre_piece <= 250):
        return tva_250_piece
    elif(nombre_piece <= 500):
        return tva_500_piece
    elif(nombre_piece > 500):
        return tva_plus_500_piece

def affichage(nombre_piece, prix_unitaire, rabais, tva, total):
    print("Nombre de pièces:", nombre_piece, "\nPrix unitaire:", prix_unitaire, "\nTaux de rabais:", rabais, "\nTaux de TVA:", tva, "\nSomme à payer:", total)

# Procédure main()
def main():
    prix_unitaire = int(input("Prix unitaire : "))
    nombre_piece = int(input("Nombre de pièce(s) : "))

    rabais = calcul_rabais(nombre_piece)
    tva = calcul_tva(nombre_piece)

    montant_rabais = (prix_unitaire * nombre_piece) * rabais / 100
    montant_tva = ((prix_unitaire * nombre_piece) - montant_rabais) * tva / 100
    total = (prix_unitaire * nombre_piece) - montant_rabais + montant_tva

    affichage(nombre_piece, prix_unitaire, rabais, tva, total)

# Appel de la procédure main()
if __name__ == "__main__":
    main()