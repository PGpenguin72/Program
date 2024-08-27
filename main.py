import time
import os 
from turtle import *
from os import system as cmd

location = os.path.dirname(__file__)
Games = os.path.join(location, "Apps")
ver = {
    "猜枚戲" : "1.0.6",
    "以緣分之組" : "1.0.1",
    "競龜戲" : "1.0.2"
}

while True:
    cmd("cls")
    print("肆，造作者企鵝 \n 版. 1.0.5 勿改")
    print("可擇之項:")

    for dirpath, dirnames, filenames in os.walk(Games):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            print(">", name)

    Uinput = input("擇一啟之 \n > > > ")
    if Uinput == "猜枚戲":
        os.chdir(Games)
        print("\n\n\n 正啟之") 
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "競龜戲":
        os.chdir(Games)
        print("\n\n\n 正啟之")
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "以緣分之組":
        os.chdir(Games)
        print("\n\n\n 正啟之")
        time.sleep(3)
        cmd("cls")
        break
    else:
        print("\n\n\n (不可以之啟之)")
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
write(arg= Uinput + "，造作者企鵝", font=style, align="center")
right(90)
forward(40)
write(arg="版. " + ver[Uinput] + "勿改", font=style, align="center")
forward(120)
write(arg="(一彈指，即始。)", font=style_2, align="left")
forward(20)
for i in range(7):
    hideturtle()
    time.sleep(0.5)
    showturtle()
    time.sleep(0.5)

clear()
bye()


if Uinput == "猜枚戲":
    os.chdir(Games)
    cmd("python 猜枚戲.py")
elif Uinput == "競龜戲":
    os.chdir(Games)
    cmd("python 競龜戲.py")
elif Uinput == "以緣分之組":
    time.sleep(3)
    cmd("cls")
    cmd("python 以緣分之組.py")
