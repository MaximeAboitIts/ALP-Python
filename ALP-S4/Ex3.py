# CONSTANTES
PRISE_EN_CHARGE_CAT_1 = 100
PRISE_EN_CHARGE_AUTRE_CAT = 200

PRIX_KILOMETRE_CAT_1 = 0.80
PRIX_KILOMETRE_CAT_2 = 1
PRIX_KILOMETRE_CAT_3 = 1.50

RABAIS = 10

# FONCTIONS
def prix_forfaitaire(categorie):
    if(categorie == 1):
        return PRISE_EN_CHARGE_CAT_1
    else:
        return PRISE_EN_CHARGE_AUTRE_CAT

def calcul_prix_km(categorie, nb_km):
    if(categorie == 1):
        return PRIX_KILOMETRE_CAT_1 * nb_km
    elif(categorie == 2):
        return PRIX_KILOMETRE_CAT_2 * nb_km
    else:
        return PRIX_KILOMETRE_CAT_3 * nb_km

def calcul_prix_final(type_client, charge_forfaitaire, prix_km):
    prix = charge_forfaitaire + prix_km
    if(type_client == "Collaborateur"):
        return prix - (prix * RABAIS / 100)
    else:
        return prix

def affichage(categorie, type_client, nb_km, prix_final):
    print(f"Catégorie: {categorie}")
    print(f"Type de client: {type_client}")
    print(f"Nombre de kilomètres: {nb_km}")
    print(f"Prix à payer: {prix_final}")

# PROGRAMME
def main():
    categorie = int(input("Choisissez une catégorie\n- 1\n- 2\n- 3\n"))
    type_client = input("Choisissez entre\n- Collaborateur\n- Client\n")
    nb_km = int(input("Entrez le nombre de KM : "))

    charge_forfaitaire = prix_forfaitaire(categorie)
    prix_km = calcul_prix_km(categorie, nb_km)
    prix_final = calcul_prix_final(type_client, charge_forfaitaire, prix_km)

    affichage(categorie, type_client, nb_km, prix_final)

main()