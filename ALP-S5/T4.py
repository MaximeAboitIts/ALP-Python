from turtle import *

# CONSTANTES


# FONCTIONS
def dessin(nombre_entier, nombre_de_trait):
    hideturtle() #pour éviter de voir la tortue bouger
    penup() #pour éviter un trait non demandé
    setpos(-400, 0) #pour démarrer plus à gauche
    pendown() #pour réactiver le dessin de la tortue
    showturtle() #pour afficher la tortue elle-même
    for i in range(nombre_de_trait):
        dot(nombre_entier)
        if i % 2 == 0:
            left(45)
        else:
            left(-45)
        forward(50)
        if i % 2 == 0:
            left(-45)
        else:
            left(45)
        dot(nombre_entier)
    done()

# PROGRAMME
def main():
    nombre_entier = int(input("Entrez un petit nombre entier : "))
    nombre_de_trait = int(input("Entrez le nombre de trait : "))
    dessin(nombre_entier, nombre_de_trait)

main()