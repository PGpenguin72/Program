import time
import os 
from turtle import *
from os import system as cmd

location = os.path.dirname(__file__)
Games = os.path.join(location, "Apps")
ver = {
    "猜拳" : "1.0.6",
    "隨機分組" : "1.0.1",
    "賽龜" : "1.0.2",
    "加解密" : "1.0.0"
}

while True:
    cmd("cls")
    print("小遊戲大集結，Made By.PGpenguin72 \n ver. 1.0.5 請勿隨意修改程序碼")
    print("目前擁有的程序:")

    for dirpath, dirnames, filenames in os.walk(Games):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            print(">", name)

    Uinput = input("請問你想玩什麼遊戲? \n > > > ")
    if Uinput == "猜拳":
        os.chdir(Games)
        print("\n\n\n 正在啟動小程序:D") 
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "賽龜":
        os.chdir(Games)
        print("\n\n\n 正在啟動小程序:D")
        time.sleep(3)
        cmd("cls")
        break
    elif Uinput == "隨機分組":
        os.chdir(Games)
        print("\n\n\n 正在啟動小程序:D")
        time.sleep(3)
        cmd("cls")
        break
    else:
        print("\n\n\n (目前不支持此軟件，請重新輸入)")
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
write(arg= Uinput + "小程序，Made By.PGpenguin72", font=style, align="center")
right(90)
forward(40)
write(arg="ver. " + ver[Uinput] + "請勿隨意修改程序碼", font=style, align="center")
forward(120)
write(arg="(五秒後即將開始執行程序)", font=style_2, align="left")
forward(20)
for i in range(5):
    hideturtle()
    time.sleep(0.5)
    showturtle()
    time.sleep(0.5)

clear()
bye()


if Uinput == "猜拳":
    os.chdir(Games)
    cmd("python 猜拳.py")
elif Uinput == "賽龜":
    os.chdir(Games)
    cmd("python 賽龜.py")
elif Uinput == "隨機分組":
    time.sleep(3)
    cmd("cls")
    cmd("python 隨機分組.py")
elif Uinput == "加解密":
    time.sleep(3)
    cmd("cls")
    cmd("python 加解密.py")