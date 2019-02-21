# coding: utf-8

import turtle
import random
import math

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.speed(0)

gotoxy(0, 0)
turtle.circle(80)
gotoxy(0, 165)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(7)
turtle.end_fill()

phi = 360 / 7
r = 50

for i in range(0, 7):
    phi_rad = phi * i * math.pi / 180.0
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 57)
    turtle.circle(21)

answer = ''
while answer != 'n':
    answer = turtle.textinput("Нарисовать окружность", "y/n")
    if answer == 'y':
        turtle.penup()
        turtle.goto(random.randrange(-300, 300), random.randrange(-200, 200))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(1, 100))
        turtle.end_fill()
    else:
        pass
