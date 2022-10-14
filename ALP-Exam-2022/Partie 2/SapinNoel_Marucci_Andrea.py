# Épreuve du 21.09.2022
# Exercice 1 – Sapin de Noël 


# Imports
from turtle import *

# Procédures et fonctions
def fleche(longueur, angle): # création de la flèche
    forward(longueur)
    right(180-angle)
    forward(longueur)
    backward(longueur)
    right(angle*2)
    forward(longueur)
    backward(longueur)
    right(180-angle)


def sapin(nombre_fleche, longueur, angle, couleur_choisis): # création d'une boucle pour répéter la création de la flèche en fonction du nombre de flèche choisis
    left(90)
    couleur_par_defaut = "green"
    for i in range(nombre_fleche):
        if i % 3 == 2: # si oui, ajouter la couleur choisis par l'utilisateur
            color(couleur_choisis)
        else: # sinon, ajouter la couleur par défaut qui est 'green'
            color(couleur_par_defaut)
        fleche(longueur, angle)
    done()

# Procédure main()
def main():
    hideturtle() # pour ne pas voir la tortue (à ne pas supprimer)
    # commencez à coder ici...
    nombre_fleche = int(input("Entrez le nombre de flèche : "))
    longueur = int(input("Entrez la longueur : "))
    angle = int(input("Entrez la valeur de l'angle : "))
    couleur_choisis = input("Choisissez une couleur : ")

    sapin(nombre_fleche, longueur, angle, couleur_choisis)

# Appel de la procédure main()
if __name__ == "__main__":
    main()
