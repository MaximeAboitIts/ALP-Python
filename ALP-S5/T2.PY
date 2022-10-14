from turtle import *

# CONSTANTES
TRIANGLE = 3
CARRE = 4
PENTAGONE = 5

# FONCTIONS
def choix_de_la_forme(nom_de_la_forme):
    if nom_de_la_forme == "Triangle":
        return TRIANGLE
    elif nom_de_la_forme == "Carré":
        return CARRE
    elif nom_de_la_forme == "Pentagone":
        return PENTAGONE

def dessin(nombre_de_cote):
    for i in range(nombre_de_cote):
        forward(100)
        left(360 / nombre_de_cote)

    done()

# PROGRAMME
def main():
    nom_de_la_forme = input("Entrez la forme a dessiner\n- Triangle\n- Carré\n- Pentagone : ")
    nombre_de_cote = choix_de_la_forme(nom_de_la_forme)

    dessin(nombre_de_cote)

main()