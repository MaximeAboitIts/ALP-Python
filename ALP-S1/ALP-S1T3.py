from turtle import *

longueur = int(input("La longueur est: "))
largeur = longueur / 2

begin_fill()
for i in range(0, 4):
     if i % 2 == 0:
         forward(longueur)
         left(90)
     else:
         forward(largeur)
         left(90)
end_fill()
done()