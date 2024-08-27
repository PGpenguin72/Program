import random
import time
import msvcrt
import json
import os
from os import system as cmd

cmd("title 石头剪刀布小程序")
print("石头剪刀布小程序，Made By.PGpenguin72 \n ver. 1.0.6 请勿随意修改程序码")
print("3秒后即将开始游戏！")

win_time = 0
round_time = 0
half = 0.5
one = 1
hundred = 100
per = 100

time.sleep(3)

while True:
    cmd("cls")
    print("++++++++++++++++++++++++++")
    print("目前游玩局数：", round_time)
    print("赢的局数：", win_time)
    print("胜率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time += one
    print("第", round_time, "局")
    player = input("选择你要出石头,剪刀还是布? (或输入stop来结算成绩) \n > > >")
    computer = random.choice(["石头", "剪刀", "布"])
    print("\n")
    W = "你赢了\n"
    L = "你输了\n\n"
    
    if player == computer:
        print("平手 \n")
        win_time += half
    elif player == "剪刀":
        if computer == "布":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "石头":
        if computer == "剪刀":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "布":
        if computer == "石头":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "stop":
        round_time -= one
        break
    else:
        print("ERROR(输入无效)\n")
        round_time -= one
        continue

    answer = "玩家:" + player + " Vs. " + "计算机:" + computer
    print("上方是对战结果")
    time.sleep(1)
    print("")
    print("下面是双方的选择")
    print(answer)

    per = win_time / round_time * hundred
    time.sleep(3)

if player == "stop" and round_time == 0:
    print("\n\n\n")
    print("石头剪刀布小程式，Made By.PGpenguin72 \n ver. 1.0.6 请勿随意修改程序码")
    print("\n\n\n按下任意键离开或关闭程序")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("请输入你的名称： \n > > >")
    cmd("cls")
    print("用户名：", name)
    print("游玩局数：", round_time)
    print("赢的局数：", win_time)
    print("胜率：", per ,"%")
    print("\n")
    if per < 50:
        print("系统:菜，就多练！输不起就别玩（x")
    else:
        print("系统:叫你骄傲了吗？人家隔壁小明玩的都比你好了骄傲个der 啊？")


    print("\n\n\n")
    print("石头剪刀布小程序，Made By.PGpenguin72 \n ver. 1.0.6 请勿随意修改程序码")
    print("\n\n\n按下任意键离开或关闭程序")
    msvcrt.getch()