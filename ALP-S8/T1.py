from turtle import *

def dessin(longueur_initiale, increment, longueur_maximale):
    speed(-1)
    couleur = ["yellow", "green", "blue", "red"]
    i = 0
    while longueur_initiale <= longueur_maximale:
        color(couleur[i%4])
        forward(longueur_initiale)
        longueur_initiale += increment
        right(90)
        i += 1
    done()

def main():
    longueur_initiale = int(input("Entrez la longueur initiale : "))
    increment = int(input("Entrez l'incrément : "))
    longueur_maximale = int(input("Entrez la longueur maximale : "))

    dessin(longueur_initiale, increment, longueur_maximale)

main()