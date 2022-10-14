from turtle import *

# CONSTANTES


# FONCTIONS
def dessin(couleur):
    color(couleur)
    dot(10)
    for i in range(4):
        forward(100)
        dot(20)
        left(180)
        forward(100)
        left(90)
    done()

# PROGRAMME
def main():
    couleur = input("Entrez le nom d'une couleur : ")
    dessin(couleur)

main()