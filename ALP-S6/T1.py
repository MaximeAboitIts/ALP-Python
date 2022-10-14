from turtle import *

nombre_point = int(input("Veuillez entrez le nombre de point (chiffre positif) : "))
taille_point = int(input("Veuillez entrez la taille des grands points (entre 10 et 50) : "))

def dessin(nombre_point, taille_point):
    for i in range(nombre_point):
        color('white')
        speed(0)
        circle(taille_point)
        left(360 / nombre_point)
        right(10)
        

    done()

bgcolor('blue')
dessin(nombre_point, taille_point)