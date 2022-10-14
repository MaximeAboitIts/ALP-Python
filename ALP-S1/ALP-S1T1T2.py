from turtle import *

#couleur1 = input("Couleur des traits ? ")
#couleur2 = input("Couleur de remplissage ? ")
# color('green', 'blue')
# color('red', 'yellow')
#color(couleur1, couleur2)

#T1
# begin_fill()
# for i in range(0, 4):
#     if i % 2 == 0:
#         forward(150)
#         left(90)
#     else:
#         forward(100)
#         left(90)
# end_fill()

#T2
begin_fill()
for i in range(0, 4):
    if i % 2 == 0:
        right(120)
    else:
        right(60)
    forward(100)
end_fill()
done()