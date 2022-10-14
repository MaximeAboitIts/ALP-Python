# Série 10, Exercice 3
# Nom et prénom: ?

''' Suite à la Course de l'Escalade qui a eu lieu ce weekend, on vous demande de faire un petit
    programme qui valide les classements, qui permet d'afficher certains résultats, ainsi que de
    modifier le temps de certains coureurs selon leur sexe.
    
    Les résultats ont été stockés dans 2 listes lors du passage de la ligne d'arrivée :
      -  une liste lst_temps contenant le temps de chaque coureur qui a franchi la ligne d'arrivée.
        Les temps sont donc stockés dans l'ordre d'arrivée (du premier au dernier).
      -  une liste lst_genre indiquant si le coureur est un homme (valeur True) ou une femme.
    Un même coureur est désigné au moyen du même indice dans les deux listes.
    
    La procédure main contient les résultats de plusieurs courses par catégorie d'âge.
    Vous pouvez donc tester les résultats des courses n°1 à 4
    
    Votre travail consiste à compléter ce script de sorte que les différentes procédures-fonctions
    respectent les spécifications données dans leurs commentaires. Vous remplacerez les commentaires
    "' A COMPLETER '" par les éléments nécessaires. '''

# Procédures et fonctions
# Fonction à résulat booléan (type = bool) retournant True si tous les temps sont dans l'ordre croissant (chaque valeur étant >= à la précédente), False sinon.
# Cette fonction doit également afficher des messages d'erreur
# Regardez les résultats produits pour la course n°4, ceux-ci indiquent le texte des messages d'erreur.
# Cette procédure reçoit en paramètre:
#    - une liste lst_temps contenant le temps de chaque coureur (type = float).


def donnees_valides(lst_temps):
    ValNbTemps = lst_temps[0]
    for ValElem in lst_temps:
        if ValElem < ValNbTemps:
            return False
        ValNbTemps = ValElem
    return True

# Procédure permettant d'afficher le n°, le temps et le nombre de coureurs Homme qui sont arrivés AVANT la 1ère Femme.
# Un message spécial indique s'il n'y a pas eu de femmes dans cette course (cf. résultats de la course n°3).
# Cette procédure reçoit en paramètre:
#    - une liste lst_temps contenant le temps de chaque coureur (type = float).
#    - une liste lst_genre contenant le genre de chaque coureur (type = bool).


def afficher_hommes_arrives_avant_1ere_femme(lst_temps, lst_genre):
    for i in range(len(lst_genre)):
        if lst_genre == lst_genre[i]:
            return False
        else:
            return True


# Procédure permettant de modifier le temps de toutes les personnes du genre indiqué.
# Cette procédure reçoit en paramètre:
#    - un code (type = bool) indiquant si on souhaite modifier le temps des Hommes (valeur True) ou des Femmes
#    - un temps (type = float) à ajouter (si positif) ou à ôter (si négatif) pour toutes les personnes du genre indiqué
#    - une liste de temps à modifier (type = float)
#    - une liste indiquant pour chaque n° s'il s'agit d'un Homme ou d'une Femme (type = bool)


def modifier_temps_selon_genre(code, temps, lst_temps, lst_genre):
    ''' A COMPLETER '''

# Procédure main()
# Permet de tester les différentes procédures et fonctions développées ci-dessus.
# Vous ne devriez pas modifier le code de cette procédure.


def main():
    no_course = int(input("Entrez un numéro de course"))

    if no_course == 1:
        lst_temps = [12.5, 12.7, 12.8, 13.2,
                     13.7, 15.1, 15.8, 15.8, 16.2, 19.7]
        lst_genre = [True, True, True, False,
                     True, True, False, False, True, True]
    elif no_course == 2:
        lst_temps = [22.5, 22.7, 22.8, 23.2,
                     23.7, 25.1, 25.8, 25.8, 26.2, 29.7]
        lst_genre = [False, True, False, True,
                     True, True, False, False, True, True]
    elif no_course == 3:
        lst_temps = [32.5, 32.7, 32.8, 33.2,
                     33.7, 35.1, 35.8, 35.8, 36.2, 39.7]
        lst_genre = [True, True, True, True,
                     True, True, True, True, True, True]
    elif no_course == 4:
        lst_temps = [42.5, 42.7, 40.8, 43.2,
                     43.7, 45.2, 45.1, 45.8, 45.8, 49.7]
        lst_genre = [True, True, False, True,
                     True, True, False, False, True, True]
    else:
        print("Erreur: no course doit être entre 1 et 4 !")
        raise SystemExit

    print("Résultats de la course n°", no_course, " : ", sep='')
    if donnees_valides(lst_temps):
        print("\nListe des hommes arrivés avant la 1ère femme :")
        afficher_hommes_arrives_avant_1ere_femme(lst_temps, lst_genre)
        modifier_temps_selon_genre(True, 1, lst_temps, lst_genre)
        print("\n--- APRÈS MODIFICATION ---")
        if donnees_valides(lst_temps):
            print("Liste des hommes arrivés avant la 1ère femme :")
            afficher_hommes_arrives_avant_1ere_femme(lst_temps, lst_genre)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
