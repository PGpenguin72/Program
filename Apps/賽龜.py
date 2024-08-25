import time
import os 
import random
import msvcrt
from random import randint
from os import system as cmd
from turtle import *

cmd("title 賽龜小程序")
cmd("cls")
print("賽龜小程式，Made By.PGpenguin72 \n ver. 1.0.2 請勿隨意修改程序碼 \n\n\n")
print("(5秒後即將開始遊戲！)")

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
    print("目前局數：", round_time)
    print("贏的局數：", win_time)
    print("勝率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time = round_time + one
    print("第", round_time, "局")
    Uinput = input("請選擇你覺得會贏的烏龜'紅、橙、黃、綠或藍'(或輸入stop來停止) \n > > >")
    if Uinput in ["紅", "橙", "黃", "綠", "藍"]:
        print("賽龜即將開始")
    elif Uinput == "stop":
        print("遊戲即將結束")
        round_time = round_time - one
        break
    else:
        tr.hideturtle()
        to.hideturtle()
        ty.hideturtle()
        tg.hideturtle()
        tb.hideturtle()
        print("請確認你輸入的文字")
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
        rank = "紅"
    if TO > TR and TO > TG and TO > TY and TO > TB:
        rank = "橙"
    if TY > TO and TY > TG and TY > TR and TY > TB:
        rank = "黃"
    if TG > TO and TG > TR and TG > TY and TG > TB:
        rank = "綠"
    if TB > TO and TB > TG and TB > TY and TB > TR:
        rank = "藍"

    if rank == Uinput:
        print("恭喜你猜中了:D \n\n\n")
        win_time = win_time + one
    elif rank == "error":
        print("系統出錯，請重新啟動遊戲 \n\n\n")
    else:
        print("喔不，你猜錯了:( 再試一次吧! \n\n\n")
    
    per = win_time / round_time * 100
    
    print("5秒後即將開始新的遊戲")
    time.sleep(3)
    tr.hideturtle()
    to.hideturtle()
    ty.hideturtle()
    tg.hideturtle()
    tb.hideturtle()

if Uinput == "stop" and round_time == 0 :
    cmd("cls")
    print("\n\n")
    print("賽龜小程式，Made By.PGpenguin72 \n ver. 1.0.2 請勿隨意修改程序碼")
    print("\n\n\n按下任意鍵離開或關閉程序")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("請輸入你的名字： \n > > >")
    cmd("cls")
    print("姓名：", name)
    print("遊玩局數：", round_time)
    print("贏的局數：", win_time)
    print("勝率：", per ,"%")
    print("\n")
    if per < 20:
        print("System:啊? 這麼簡單的遊戲也可以輸成這樣?")
    else:
        print("System:厲害! 本作者都沒辦法玩到這麼高分呢:D")


    print("\n\n")
    print("賽龜小程式，Made By.PGpenguin72 \n ver. 1.0.2 請勿隨意修改程序碼")
    print("\n\n\n按下任意鍵離開或關閉程序")
    msvcrt.getch()
