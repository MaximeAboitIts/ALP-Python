# Épreuve du 29.09.2021
# Nom et prénom:

from turtle import *

### CODE FOURNI -- NE PAS MODIFIER 

# my_dot dessine un point d'une certaine largeur et d'une certaine couleur
def my_dot(my_width, my_color): 
    previous_color = pencolor() # pour ne pas modifier la couleur d'autre chose que le point
    color(my_color)
    dot(my_width)
    color(previous_color) # pour ne pas modifier la couleur d'autre chose que le point

# my_init initialise les paramètres par défaut
def my_init():
    penup() # pour ne pas dessiner autre chose que des points
    hideturtle() # pour ne pas voir la tortue
    goto(-100, 200) # pour ne pas démarrer au centre et
                    # permettre des dessins plus larges
    
### fin des procédures fournies
### Votre code **après** ce commentaire                    

def couleur(c):
    if c == 0:
        return "blue"
    elif c == 1:
        return "orange"
    elif c == 2:
        return "red"

def polydot(nombre, cote):
    my_init() # obligatoirement en première instruction -- ne pas effacer !
    taile_grande = True
    for c in range(nombre):
        forward(cote)
        la_couleur = couleur(c%3)
        if taile_grande:
            my_dot(cote, la_couleur)
            taile_grande = False
        else:
            my_dot(cote * 0.6, la_couleur)
            taile_grande = True
        right(360/nombre)
    done()

#Pour information
#Boucle de base pour dessiner des polygones
#  for c in range(nbCotes):
#      forward(tailleCote)
#      right(360/nbCotes)




### NE PAS MODIFIER ce qui suit !
nb_points = int(input("Combien de points ? "))
taille_cote = int(input("Quelle taille pour un grand point ? "))
# NB : la taille d'un (grand) point est aussi la taille d'un côté
polydot(nb_points, taille_cote)