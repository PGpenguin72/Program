import time
import os 
import random
import msvcrt
from random import randint
from os import system as cmd
from turtle import *

cmd("title Turtle Racing")
cmd("cls")
print("Turtle Racing, Made By.PGpenguin72 \n ver. 1.0.2 Do not modify the code arbitrarily. \n\n\n")
print("(Game starts in 5 seconds!)")

t = "turtle"
raw = -250
center = int(115)
thirty = int(30)
rank = "error"
win_time = 0
round_time = 0
one = 1 
per = 100

penup()
goto(-250,140)
speed(0)
for step in range(26):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


while True:

    tr = Turtle()
    tr.color("red")
    tr.shape(t)
    tr.penup()
    tr.goto(-270, center)
    center = center - thirty
    to = Turtle()
    to.color("orange")
    to.shape(t)
    to.penup()
    to.goto(-270, center)
    center = center - thirty
    ty = Turtle()
    ty.color("yellow")
    ty.shape(t)
    ty.penup()
    ty.goto(-270, center)
    center = center - thirty
    tg = Turtle()
    tg.color("green")
    tg.shape(t)
    tg.penup()
    tg.goto(-270, center)
    center = center - thirty
    tb = Turtle()
    tb.color("blue")
    tb.shape(t)
    tb.penup()
    tb.goto(-270, center)
    center = int(115)

    cmd("cls")
    print("++++++++++++++++++++++++++")
    print("Round Time:", round_time)
    print("Win Time:", win_time)
    print("Wining Rate:", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time = round_time + one
    print("Round ", round_time)
    Uinput = input("Choose which color of the turtle will be the winner 'Red, Orange, Yellow, Green or Blue'(or enter stop to end the game) \n > > >")
    if Uinput in ["Red", "Orange", "Yellow", "Green", "Blue"]:
        print("Turtle Racing is about to start")
    elif Uinput == "stop":
        print("The game is about to come to an end")
        round_time = round_time - one
        break
    else:
        tr.hideturtle()
        to.hideturtle()
        ty.hideturtle()
        tg.hideturtle()
        tb.hideturtle()
        print("Please check the text you entered ")
        round_time = round_time - one
        continue

    for turn in range(100):
        tr.forward(randint(1,7))
        to.forward(randint(1,7))
        ty.forward(randint(1,7))
        tg.forward(randint(1,7))
        tb.forward(randint(1,7))

    TR = tr.xcor()
    TR = round(TR, 0)
    TO = to.xcor()
    TO = round(TO, 0)
    TY = ty.xcor()
    TY = round(TY, 0)
    TG = tg.xcor()
    TG = round(TG, 0)
    TB = tb.xcor()
    TB = round(TB, 0) 

    if TR > TO and TR > TG and TR > TY and TR > TB:
        rank = "Red"
    if TO > TR and TO > TG and TO > TY and TO > TB:
        rank = "Orange"
    if TY > TO and TY > TG and TY > TR and TY > TB:
        rank = "Yellow"
    if TG > TO and TG > TR and TG > TY and TG > TB:
        rank = "Green"
    if TB > TO and TB > TG and TB > TY and TB > TR:
        rank = "Blue"

    if rank == Uinput:
        print("Congrats! Nice guess! :D \n\n\n")
        win_time = win_time + one
    elif rank == "error":
        print("ERROR. Please restart the game. \n\n\n")
    else:
        print("Oh no, wrong guess :( Try it again! \n\n\n")
    
    per = win_time / round_time * 100
    
    print("New game will start in 5 seconds")
    time.sleep(3)
    tr.hideturtle()
    to.hideturtle()
    ty.hideturtle()
    tg.hideturtle()
    tb.hideturtle()

if Uinput == "stop" and round_time == 0 :
    cmd("cls")
    print("\n\n")
    print("Turtle Racing, Made By.PGpenguin72 \n ver. 1.0.2 Do not modify the code arbitrarily.")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("Please enter your name: \n > > >")
    cmd("cls")
    print("Name:", name)
    print("Round Time:", round_time)
    print("Win Time:", win_time)
    print("Winning Rate", per ,"%")
    print("\n")
    if per < 20:
        print("System: Huh? You're impossible!")
    else:
        print("System: You rock!  You're really something! :D")


    print("\n\n")
    print("Turtle Racing, Made By.PGpenguin72 \n ver. 1.0.2 Do not modify the code arbitrarily.")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()
