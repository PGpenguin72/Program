import time
import os 
from turtle import *
from os import system as cmd

location = os.path.dirname(__file__)
Games = os.path.join(location, "Apps")
ver = {
    "Paper-Scissors-Stone": "1.0.6",
    "Random Grouping": "1.0.1",
    "Turtle Racing": "1.0.2"
}

while True:
    cmd("cls")
    print("Mini Program UNITE, Made By. PGpenguin72\n ver. 1.0.5 Do not modify the code arbitrarily")
    print("Available programs by far:")

    for dirpath, dirnames, filenames in os.walk(Games):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            print(">", name)

    Uinput = input("Which game do you want to play? \n > > > ")
    if Uinput == "Paper-Scissors-Stone":
        os.chdir(Games)
        print("\n\n\n program booting :D") 
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "Turtle Racing":
        os.chdir(Games)
        print("\n\n\n mini program booting :D")
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "Random Grouping":
        os.chdir(Games)
        print("\n\n\n program booting :D")
        time.sleep(3)
        cmd("cls")
        break
    else:
        print("\n\n\n (Software unsupported, please re-enter)")
        time.sleep(3)
        continue


Colors = {
    "Red" : "#ff0000",
    "Orange" : "#ff4500",
    "Yellow" : "#ffff00",
    "Green" : "#008000",
    "Blue" : "#0000ff",
    "Indigo" : "#4b0082",
    "Purple" : "#800080",
    "Black" : "#000000",
    "White" : "#ffffff",
    "Gray" : "#808080"
}
style = ("Courier", 15, "bold")
style_2 = ("Courier", 10, "bold")

screen = Screen()
screen.setup(500,500)
screen.bgcolor(Colors["Black"])
color(Colors["White"])
dot(480)

penup()
goto(0,50)
speed(0)
color(Colors["Black"])
write(arg= Uinput + "Mini Program, Made By. PGpenguin72", font=style, align="center")
right(90)
forward(40)
write(arg="ver. " + ver[Uinput] + "Do not modify the code arbitrarily", font=style, align="center")
forward(120)
write(arg="(Program will be executed in five seconds)", font=style_2, align="left")
forward(20)
for i in range(5):
    hideturtle()
    time.sleep(0.5)
    showturtle()
    time.sleep(0.5)

clear()
bye()


if Uinput == "Paper-Scissors-Stone":
    os.chdir(Games)
    cmd("python Paper-Scissors-Stone.py")
elif Uinput == "Turtle Racing":
    os.chdir(Games)
    cmd("python Turtle Racing.py")
elif Uinput == "Random Grouping":
    time.sleep(3)
    cmd("cls")
    cmd("python Random Grouping.py")
