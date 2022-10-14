# Imports

# Constantes
TYPE_DE_PLACE_DEBOUT = "places debout"
TYPE_DE_PLACE_ASSIS = "places assises"

PRIX_PLACE_DEBOUT = 20
PRIX_PLACE_ASSISES = 30
# Procédures et fonctions
def calcul_prix(type_de_place, nombre_de_place):
    if(type_de_place == TYPE_DE_PLACE_ASSIS):
        if(nombre_de_place >= 9):
            return (nombre_de_place - 2) * PRIX_PLACE_ASSISES
        elif(nombre_de_place >= 5):
            return (nombre_de_place - 1) * PRIX_PLACE_ASSISES
        else:
            return nombre_de_place * PRIX_PLACE_ASSISES
    elif(type_de_place == TYPE_DE_PLACE_DEBOUT):
        return nombre_de_place * PRIX_PLACE_DEBOUT

def affichage(prix_final, nombre_de_place, type_de_place):
    print(f"Le prix à payer pour {nombre_de_place} {type_de_place} : {prix_final} Frs")

# Procédure main()
def main():
    type_de_place = input(f"Veuillez choisir entre\n- {TYPE_DE_PLACE_DEBOUT}\n- {TYPE_DE_PLACE_ASSIS}\n")
    nombre_de_place = int(input("Combien de place voulez-vous réserver ? "))

    prix_final = calcul_prix(type_de_place, nombre_de_place)
    affichage(prix_final, nombre_de_place, type_de_place)

# Appel de la procédure main()
if __name__ == "__main__":
    main()