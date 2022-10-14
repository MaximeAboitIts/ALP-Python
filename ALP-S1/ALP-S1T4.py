from turtle import *

choix = input("Choisisez entre\n- Carré\n- Ligne droite\n Votre choix: ")

begin_fill()
if(choix == "Carré"):
    for i in range(0, 4):
        forward(100)
        left(90)
elif(choix == "Ligne droite"):
    forward(100)
else:
    print("Aucun choix reconnu")
end_fill()
done()