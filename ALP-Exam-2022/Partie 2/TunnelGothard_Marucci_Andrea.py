# Épreuve du 21.09.2022
# Exercice 2 – Tunnel du Gothard


# Constantes
CATEGORIE_VOITURE = "une voiture" 
CATEGORIE_CAMIONS_SANS_REMORQUE = "un camion"
CATEGORIE_CAMIONS_AVEC_REMORQUE = "un camion avec remorque"

PRIX_VOITURE = 15
PRIX_CAMIONS_MOINS_DE_4_TONNES = 15
PRIX_CAMIONS_MOINS_DE_10_TONNES = 20
PRIX_CAMIONS_ENTRE_10_ET_25_TONNES = 30
PRIX_CAMIONS_ENTRE_26_ET_38_TONNES = 42
PRIX_CAMIONS_PLUS_DE_38_TONNES = 50

TAXE_CAMIONS_SUPERIEUR_A_8_METRE = 5

SUPPLEMENT_CAMIONS__REMORQUE = 30

# Procédures et fonctions
def prix_en_fonction_du_poids(poids): # vérifier quel prix correspond en fonction du poids
    if poids < 4:
        return PRIX_CAMIONS_MOINS_DE_4_TONNES
    elif poids < 10:
        return PRIX_CAMIONS_MOINS_DE_10_TONNES
    elif poids >= 10 and poids <= 25:
        return PRIX_CAMIONS_ENTRE_10_ET_25_TONNES
    elif poids >= 26 and poids <= 38:
        return PRIX_CAMIONS_ENTRE_26_ET_38_TONNES
    else:
        return PRIX_CAMIONS_PLUS_DE_38_TONNES

def prix_en_fonction_de_la_longueur(longueur): # vérifier si la longueur est supérieur à 8, si oui ajouter la taxe
    if longueur > 8:
        return (longueur - 8) * TAXE_CAMIONS_SUPERIEUR_A_8_METRE
    else:
        return 0

def prix_billet(categorie, longueur, poids): # vérifier quel est la catégorie puis calculer le prix du billet
    if categorie == 1:
        return PRIX_VOITURE
    elif categorie == 2 or categorie == 3:
        prix_poids = prix_en_fonction_du_poids(poids)
        prix_longueur = prix_en_fonction_de_la_longueur(longueur)
        prix_poids_plus_longueur = prix_poids + prix_longueur
        if categorie == 3: # vérifier si le véhicule est de la catégorie 3, si oui ajouter le supplement
            return prix_poids_plus_longueur * SUPPLEMENT_CAMIONS__REMORQUE / 100 + prix_poids_plus_longueur
        return prix_poids_plus_longueur

def nom_de_la_categorie(categorie): # vérifier la catégorie pour renvoyer le nom du véhicule
    if categorie == 1:
        return CATEGORIE_VOITURE
    elif categorie == 2:
        return CATEGORIE_CAMIONS_SANS_REMORQUE
    elif categorie == 3:
        return CATEGORIE_CAMIONS_AVEC_REMORQUE

def affichage(nom_categorie, prix_final): # afficher le message dans la console
    print(f"Le véhicule est {nom_categorie}")
    print(f"Le prix total du billet est de {prix_final} CHF")

# Procédure main()
def main():
    categorie = int(input("Entrez une catégorie : "))
    longueur = int(input("Entrez la longueur : "))
    poids = int(input("Entrez le poids : "))

    nom_categorie = nom_de_la_categorie(categorie)
    prix_final = prix_billet(categorie, longueur, poids)

    affichage(nom_categorie, prix_final)

# Appel de la procédure main()
if __name__ == "__main__":
    main()
