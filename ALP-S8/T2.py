from turtle import *

def triangle(longueur_cote):
    for i in range(2):
        forward(longueur_cote)
        left(120)


def dessin(longueur_cote):
    speed(-1)
    hideturtle()

    while longueur_cote >= 3:
        triangle(longueur_cote)

    done()

def main():
    longueur_cote = int(input("Entrez la longueur du côté : "))
    dessin(longueur_cote)

main()