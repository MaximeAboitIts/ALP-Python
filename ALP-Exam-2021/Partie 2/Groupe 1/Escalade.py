# Épreuve du 29.09.2021
# Nom et prénom: 

# Imports éventuels après ce commentaire

# Constantes éventuelles après ce commentaire
''' A COMPLETER '''
PRIX_ENTREE_SANS_DEGUISEMENT = 15
PRIX_ENTREE_AVEC_DEGUISEMENT = 10
NOMBRE_ENTREE_GRATUITE = 1
ENTRE_GRATUITE_A_PARTIR_DE = 4

BOISSONS_SUPP = 7


# Procédures et fonctions
''' A COMPLETER '''
def calcul_prix_entré(nombre_de_personne, type_de_personne):
    if type_de_personne == 1 and nombre_de_personne >= ENTRE_GRATUITE_A_PARTIR_DE:
        return (nombre_de_personne - NOMBRE_ENTREE_GRATUITE) * PRIX_ENTREE_AVEC_DEGUISEMENT
    elif type_de_personne == 1:
        return nombre_de_personne * PRIX_ENTREE_AVEC_DEGUISEMENT
    else:
        return nombre_de_personne * PRIX_ENTREE_SANS_DEGUISEMENT

def calcul_prix_final(nombre_boissons, prix_entré):
    return prix_entré + (nombre_boissons * BOISSONS_SUPP)

def calcul_boisson_offerte(prix_final, nombre_de_personne, nombre_boissons):
    if prix_final < 50:
        return nombre_de_personne + nombre_boissons
    else:
        bouteille_offerte = 1
        if prix_final >= 100:
            bouteille_offerte += prix_final // 100
        return bouteille_offerte + nombre_de_personne + nombre_boissons

def affichage(nombre_de_boisson_offerte, nombre_de_personne, prix_final):
    print(f"Entrée pour {nombre_de_personne} personnes, Bon pour {nombre_de_boisson_offerte} boissons, Prix à payer : {prix_final}.-")

def check_erreur(nombre_de_personne, nombre_boissons):
    nombre_de_boissons_max = nombre_de_personne * 5
    if nombre_de_personne <= 0 or nombre_de_personne > 100 or nombre_boissons <= 0 or nombre_de_boissons_max < nombre_boissons:
        return True
    else:
        return False

# Procédure executer()
def executer():
    ''' A COMPLETER '''
    nombre_de_personne = int(input("Entrez le nombre de personne : "))
    type_de_personne = int(input("Entrez le type de personne\nSi vous êtes déguisés tapez 1\nSi vous n'êtes pas déguisé tapez 2 : "))
    nombre_boissons = int(input("Combien de boissons voulez-vous commandé : "))

    error = check_erreur(nombre_de_personne, nombre_boissons)

    if error:
        print("Error!")
    else:
        prix_entré = calcul_prix_entré(nombre_de_personne, type_de_personne)
        prix_final = calcul_prix_final(nombre_boissons, prix_entré)
        nombre_de_boisson_offerte = calcul_boisson_offerte(prix_final, nombre_de_personne, nombre_boissons)
        affichage(nombre_de_boisson_offerte, nombre_de_personne, prix_final)


# Appel de la procédure main() - NE PAS MODIFIER
executer()
