# Série 10, Exercice 2
# Nom et prénom: ?

''' L'ESIG vous mandate pour réaliser un outil de gestion des notes d’étudiants.
    Vous devez réaliser sa première version en respectant les spécifications fournies.
    L’outil permet de travailler sur les résultats obtenus lors d’une épreuve par une classe d’étudiants.
    Une structure de données permet de stocker des notes. Les notes sont considérées comme des valeurs entières.
    La valeur 0 signifie qu'il n'y a pas de note pour cet étudiant.
    Pour la version suisse, les notes vont de 1 à 6, avec la limite du suffisant à 4.
    (Il est prévu d'en faire par la suite une version pour la France, où les notes vont de 0 à 20, avec la limite du suffisant à 10.) '''

# Constantes
from multiprocessing.connection import Client
from turtle import circle


NOTE_OK = 0
AUCUNE_NOTE = 1
NOTE_INVALIDE = -2
QUE_DES_INSUFFISANTS = -3
NOTE_MIN = 1
NOTE_MAX = 6
LIMITE_SUFFISANT = 4

# Procédures et fonctions
# Fonction à résulat entier (type = int) permettant d'analyser les notes fournies en paramètre (des entiers) et de retourner un code correspondant à cette analyse:
#    - si aucune note n’est présente dans la structure (que des 0) :                            retourne AUCUNE_NOTE
#    - s'il y a une note (ou plus) qui n’est pas comprise entre 1 et 6 inclus :                 retourne NOTE_INVALIDE
#    - si toutes les notes sont strictement inférieures à 4 :                                   retourne QUE_DES_INSUFFISANTS
#    - dans tous les autres cas: (toutes les notes sont valides et il y a des notes >= 4) :     retourne NOTE_OK
# Cette procédure reçoit en paramètre:
#    - une liste lst_notes contenant les notes de chaque étudiant (type = int).


def analyse_des_notes(lst_notes):
    ValNbValeur0 = 0
    ValNbValeur1et6 = 0
    ValNbInf4 = 0

    for i in range(len(lst_notes)):
        if lst_notes[i] == 0:
            ValNbValeur0 = ValNbValeur0 + 1
        if lst_notes[i] >= NOTE_MIN and lst_notes[i] <= NOTE_MAX:
            return NOTE_INVALIDE
        if lst_notes[i] <= LIMITE_SUFFISANT:
            ValNbInf4 = ValNbInf4 + 1

    if ValNbValeur0 == len(lst_notes):
        return AUCUNE_NOTE
    elif ValNbValeur1et6 != len(lst_notes):
        return NOTE_INVALIDE
    elif ValNbInf4 == len(lst_notes):
        return NOTE_OK

    return 0
# Procédure permettant d'afficher la statistique des notes, c’est-à-dire le nombre d’apparitions de chaque note (6,5,4,3,2,1) fournies en paramètre.
# Cette procédure reçoit en paramètre:
#    - une liste lst_notes contenant les notes de chaque étudiant (type = int).
# Exemple :
#    Nombre de 6 : 3
#    Nombre de 5 : 2
#    Nombre de 4 : 3
#    Nombre de 3 : 0
#    Nombre de 2 : 1
#    Nombre de 1 : 0


def afficher_statistique(lst_notes):
    # ValNb1 = 0
    # ValNb2 = 0
    # ValNb3 = 0
    # ValNb4 = 0
    # ValNb5 = 0
    # ValNb6 = 0

    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 1:
    #         ValNb1 += 1
    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 2:
    #         ValNb2 += 1
    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 3:
    #         ValNb3 += 1
    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 4:
    #         ValNb4 += 1
    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 5:
    #         ValNb5 += 1
    # for i in range(len(lst_notes)):
    #     if lst_notes[i] == 6:
    #         ValNb6 += 1

    # ValNbList = [ValNb1, ValNb2, ValNb3, ValNb4, ValNb5, ValNb6]

    # for i in range(len(ValNbList)):
    #     print(f"Nombre de {i + 1} : {ValNbList[i]}")

    for i in range(6, 0, -1):
        ValNbRange = 0
        for x in range(len(lst_notes)):
            if lst_notes[x] == i:
                ValNbRange = ValNbRange + 1
        print(f"Nombre de {i} : {ValNbRange}")

# Procédure main()
# Test des procédures à développer. Ne doit (en principe) pas être modifiée.


def main():
    lst_notes = list(map(int, input("Entrez une liste de notes").split()))
    code = analyse_des_notes(lst_notes)
    if code == NOTE_OK:
        print("Les notes sont correctes.")
    elif code == AUCUNE_NOTE:
        print("Aucune note !")
    elif code == NOTE_INVALIDE:
        print("Les notes ne sont pas toutes valides !")
    else:
        print("Il n'y a que des insuffisants !")
    print("Statistique :")
    afficher_statistique(lst_notes)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
