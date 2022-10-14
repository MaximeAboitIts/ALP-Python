# Imports

# Constantes
PIANO_TYPE_1 = "piano droit"
PIANO_TYPE_2 = "piano à queue"

PRIX_PAR_ETAGE_PIANO_DROIT = 60
PRIX_PAR_ETAGE_PIANO_QUEUE = 90

PRIX_MAX_ETAGE_PIANO_DROIT = 600
PRIX_MAX_ETAGE_PIANO_QUEUE = 900

PRIX_PAR_KM = 6

PRIX_MINIMUM = 200
PRIX_MAXIMUM = 2500
# Procédures et fonctions

def calcul_prix_final(prix_km, prix_etage):
    prix = prix_km + prix_etage
    if(prix < PRIX_MINIMUM):
        return PRIX_MINIMUM
    elif(prix > PRIX_MAXIMUM):
        return PRIX_MAXIMUM
    else:
        return prix

def calcul_prix_etage(type_piano, total_etage):
    if(total_etage > 10):
        if(type_piano == PIANO_TYPE_1):
            return PRIX_MAX_ETAGE_PIANO_DROIT
        elif(type_piano == PIANO_TYPE_2):
            return PRIX_MAX_ETAGE_PIANO_QUEUE
    elif(type_piano == PIANO_TYPE_1):
        return total_etage * PRIX_PAR_ETAGE_PIANO_DROIT
    elif(type_piano == PIANO_TYPE_2):
        return total_etage * PRIX_PAR_ETAGE_PIANO_QUEUE

def affichage(type_piano, prix_km, prix_final, nmb_km):
    print(f"Prix total à payer pour un {type_piano} : {prix_final}.- (dont {prix_km}.- de transport pour les {nmb_km} km)")

# Procédure main()
def main():
    nmb_etage_descendu = int(input("Veuillez entrer le nombre d'étage descendu: "))
    nmb_etage_monter = int(input("Veuillez entrer le nombre d'étage à monter: "))
    type_piano = input(f"Veuillez entrer le type du piano ({PIANO_TYPE_1}, {PIANO_TYPE_2}) : ")
    nmb_km = int(input("Veuillez entrer le nombre de km: "))
    total_etage = nmb_etage_descendu + nmb_etage_monter

    prix_km = nmb_km * PRIX_PAR_KM
    prix_etage = calcul_prix_etage(type_piano, total_etage)
    prix_final = calcul_prix_final(prix_km, prix_etage)

    affichage(type_piano, prix_km, prix_final, nmb_km)

# Appel de la procédure main()
if __name__ == "__main__":
    main()