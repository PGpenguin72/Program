import random
import time
import msvcrt
import json
import os
from os import system as cmd

cmd("title 猜拳小程序")
print("猜拳小程式，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")
print("3秒後即將開始遊戲！")

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
    print("目前局數：", round_time)
    print("贏的局數：", win_time)
    print("勝率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time += one
    print("第", round_time, "局")
    player = input("選擇你要出剪刀,石頭,還是布? (或輸入stop來結算成績) \n > > >")
    computer = random.choice(["剪刀", "石頭", "布"])
    print("\n")
    W = "你贏了\n"
    L = "你輸了\n\n"
    
    if player == computer:
        print("平局 \n")
        win_time += half
    elif player == "剪刀":
        if computer == "布":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "石頭":
        if computer == "剪刀":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "布":
        if computer == "石頭":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "stop":
        round_time -= one
        break
    else:
        print("ERROR(無效回答)\n")
        round_time -= one
        continue

    answer = "玩家:" + player + " Vs. " + "電腦:" + computer
    print("上面是對戰結果")
    time.sleep(1)
    print("")
    print("下面是雙方的選擇")
    print(answer)

    per = win_time / round_time * hundred
    time.sleep(3)

print("\n\n\n")
name = input("請輸入你的名字： \n > > >")
cmd("cls")
print("姓名：", name)
print("遊玩局數：", round_time)
print("贏的局數：", win_time)
print("勝率：", per ,"%")
print("\n")
if per < 50:
    print("System:蔡，就多練！輸不起就別玩（誤")
else:
    print("System:好哦好哦，阿不就好棒棒（誤")


print("\n\n\n")
print("猜拳小程式，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")
print("\n\n\n按下任意鍵離開或關閉程序")
msvcrt.getch()