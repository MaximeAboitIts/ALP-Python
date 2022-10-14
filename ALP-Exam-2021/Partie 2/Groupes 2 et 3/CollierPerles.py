# Épreuve du 29.09.2021
# Nom et prénom:

# Imports
from turtle import *

# Procédures et fonctions
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
    
### fin du code fourni
### Votre code après ce commentaire                    

def polydot(nombre, cote):
    my_init() # obligatoirement en première instruction -- ne pas effacer !
    ''' A CODER '''
    
#Pour information
#Boucle de base pour dessiner des polygones
#  for c in range(nbCotes):
#      forward(tailleCote)
#      right(360/nbCotes)



### NE PAS MODIFIER ce qui suit !
# définition de la procédure main()
def main():
    nb_points = int(input("Combien de points ? "))
    taille_cote = int(input("Quelle taille pour un grand point ? "))
    # NB : la taille d'un gros point est aussi la taille d'un côté
    polydot(nb_points, taille_cote)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()
    
