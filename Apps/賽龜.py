import time
import os 
import random
import msvcrt
from random import randint
from os import system as cmd
from turtle import *

cmd("title 赛龟小程序")
cmd("cls")
print("赛龟小程序，Made By.PGpenguin72 \n ver. 1.0.2 请勿随意修改程序码 \n\n\n")
print("(5秒后开始游戏！)")

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
    print("目前局数：", round_time)
    print("赢的局数：", win_time)
    print("胜率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time = round_time + one
    print("第", round_time, "局")
    Uinput = input("请选择可能跑第一的乌龟'红、橙、黄、绿或蓝'(或输入stop来停止) \n > > >")
    if Uinput in ["红", "橙", "黄", "绿", "蓝"]:
        print("赛龟即将开始")
    elif Uinput == "stop":
        print("游戏即将结束")
        round_time = round_time - one
        break
    else:
        tr.hideturtle()
        to.hideturtle()
        ty.hideturtle()
        tg.hideturtle()
        tb.hideturtle()
        print("请确认你输入的信息")
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
        rank = "红"
    if TO > TR and TO > TG and TO > TY and TO > TB:
        rank = "橙"
    if TY > TO and TY > TG and TY > TR and TY > TB:
        rank = "黄"
    if TG > TO and TG > TR and TG > TY and TG > TB:
        rank = "绿"
    if TB > TO and TB > TG and TB > TY and TB > TR:
        rank = "蓝"

    if rank == Uinput:
        print("恭喜你猜中了:D \n\n\n")
        win_time = win_time + one
    elif rank == "error":
        print("系统出错，请重新运行 \n\n\n")
    else:
        print("猜错了就再试一次啊，1/5的概率，行不行啊你？ \n\n\n")
    
    per = win_time / round_time * 100
    
    print("5秒后即将开始新的回合")
    time.sleep(3)
    tr.hideturtle()
    to.hideturtle()
    ty.hideturtle()
    tg.hideturtle()
    tb.hideturtle()

if Uinput == "stop" and round_time == 0 :
    cmd("cls")
    print("\n\n")
    print("赛龟小程序，Made By.PGpenguin72 \n ver. 1.0.2 请勿随意修改程序码")
    print("\n\n\n按下任意键离开或关闭程序")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("请输入你的用户名： \n > > >")
    cmd("cls")
    print("用户名：", name)
    print("游玩局数：", round_time)
    print("赢的局数：", win_time)
    print("胜率：", per ,"%")
    print("\n")
    if per < 20:
        print("System:啊? 这游戏又咋难吗？还不是轻轻松松？咋可以输成这副狗样")
    else:
        print("System:我让你骄傲了吗？ 有这时间玩游戏不如去多读点书，清华北大还会难上吗？")


    print("\n\n")
    print("赛龟小程序，Made By.PGpenguin72 \n ver. 1.0.2 请勿随意修改程序码")
    print("\n\n\n按下任意键离开或关闭程序")
    msvcrt.getch()
