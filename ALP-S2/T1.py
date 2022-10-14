from turtle import *


def i_grec():
    forward(100)
    left(30)
    forward(100)
    left(180)
    forward(100)
    left(120)
    forward(100)


def double_i_grec():
    forward(100)
    left(30)
    i_grec()
    left(180)
    forward(100)
    left(30)
    forward(100)
    left(120)
    i_grec()


def triple_i_grec():
    forward(100)
    left(30)
    double_i_grec()
    left(180)
    forward(100)
    left(30)
    forward(100)
    left(30)
    forward(100)
    left(120)
    double_i_grec()


left(90)
# i_grec()
# double_i_grec()
triple_i_grec()
done()
