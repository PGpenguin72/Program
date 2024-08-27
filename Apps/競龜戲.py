import time
import os 
import random
import msvcrt
from random import randint
from os import system as cmd
from turtle import *

cmd("title 競龜戲")
cmd("cls")
print("競龜戲，造作者企鵝 \n 版. 1.0.2 勿改 \n\n\n")
print("一彈指，即始。")

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
    print("戲回：", round_time)
    print("贏回：", win_time)
    print("勝之率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time = round_time + one
    print(round_time, "之回")
    Uinput = input("擇一龜之色（赤、橙、黃、翠、蒼），以揣之勝。(亦以停為止) \n > > >")
    if Uinput in ["赤", "橙", "黃", "翠", "蒼"]:
        print("競龜始")
    elif Uinput == "停":
        print("競龜止")
        round_time = round_time - one
        break
    else:
        tr.hideturtle()
        to.hideturtle()
        ty.hideturtle()
        tg.hideturtle()
        tb.hideturtle()
        print("不可以之答，擇一色或止。")
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
        rank = "赤"
    if TO > TR and TO > TG and TO > TY and TO > TB:
        rank = "橙"
    if TY > TO and TY > TG and TY > TR and TY > TB:
        rank = "黃"
    if TG > TO and TG > TR and TG > TY and TG > TB:
        rank = "翠"
    if TB > TO and TB > TG and TB > TY and TB > TR:
        rank = "蒼"

    if rank == Uinput:
        print("揣中也 \n\n\n")
        win_time = win_time + one
    elif rank == "error":
        print("覆戲以始 \n\n\n")
    else:
        print("揣誤也。 \n\n\n")
    
    per = win_time / round_time * 100
    
    print("彈指間即始新戲。")
    time.sleep(3)
    tr.hideturtle()
    to.hideturtle()
    ty.hideturtle()
    tg.hideturtle()
    tb.hideturtle()

if Uinput == "stop" and round_time == 0 :
    cmd("cls")
    print("\n\n")
    print("競龜戲，造作者企鵝 \n 版. 1.0.2 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("敢問高姓？： \n > > >")
    cmd("cls")
    print("儒：", name)
    print("戲回：", round_time)
    print("贏回：", win_time)
    print("勝之率：", per ,"%")
    print("\n")
    if per < 20:
        print("算盤: 易戲亦可敗之樣？智憂矣")
    else:
        print("算盤: 勝造作者，且記勿驕矣")


    print("\n\n")
    print("競龜戲，造作者企鵝 \n 版. 1.0.2 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()
