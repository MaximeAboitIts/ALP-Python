catalogue = ["ADC-1234", "ADC-3241", "ADC-9987"]
stock = ["ADC-1234", "ADC-3241", "ADC-9987", "ADC-1234"]


def afficher_msg(code_erreur, valeur, position):
    """
    Affiche un message correspondant à un code erreur et une valeur
    paramètres : code_erreur et valeur
    """

    if code_erreur == 1:
        print("Article inconnu : ", valeur, " à la position ", position)
    elif code_erreur == 2:
        print("Article en double : ", valeur, " à la position ", position)
    elif code_erreur == 3:
        print("Stock correct : ", valeur, " articles")
    elif code_erreur == 4:
        print("Il y a ", valeur, " erreurs dans le stock")


def controler_le_stock(stock, catalogue):
    """
    Contrôle le contenu de la liste stock et affiche un message (appel de la procédure afficher_msg) avec un code correspondant à cette analyse :
    pour chaque article du stock inconnu dans le catalogue :
        Appel afficher_msg avec code_erreur = INCONNU, valeur = n° article, position = indice dans stock
    pour chaque article apparaissant plusieurs fois dans le stock :
        Appel afficher_msg avec code_erreur = MULTIPLE, valeur = n° article, position = indice dans stock
    à la fin du contrôle, si aucune erreur n'a été détectée :
        Appel afficher_msg avec code_erreur = OK, valeur = nombre d'articles dans le stock
    par contre, si une ou plusieurs erreurs ont été détectées :
        Appel afficher_msg avec code_erreur = TOTAL, valeur = nombre d'erreurs détectées.
    """

    nb_erreurs = 0
    for i in range(len(stock)):
        if stock[i] not in catalogue:
            afficher_msg(1, stock[i], i)
            nb_erreurs += 1
        elif stock.count(stock[i]) > 1:
            afficher_msg(2, stock[i], i)
            nb_erreurs += 1

    if nb_erreurs == 0:
        afficher_msg(3, len(stock), 0)
    else:
        afficher_msg(4, nb_erreurs, 0)


controler_le_stock(stock, catalogue)
