import random
import time
import msvcrt
import json
import os
from os import system as cmd

cmd("title 猜枚戲")
print("猜枚戲，造作者企鵝 \n 版. 1.0.6 勿改")
print("一彈指，即始。")

win_time = 0
round_time = 0
half = 0.5
one = 1
hundred = 100
per = 100

time.sleep(7)

while True:
    cmd("cls")
    print("++++++++++++++++++++++++++")
    print("戲回：", round_time)
    print("勝回：", win_time)
    print("勝之率：", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time += one
    print(round_time, "之回")
    player = input("擇一之予答，石，剪，亦布? (以停命其止且計級) \n > > >")
    computer = random.choice(["石", "剪", "布"])
    print("\n")
    W = "儒勝矣\n"
    L = "儒敗矣\n\n"
    
    if player == computer:
        print("不分上下 \n")
        win_time += half
    elif player == "剪":
        if computer == "布":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "石":
        if computer == "剪":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "布":
        if computer == "石":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "停":
        round_time -= one
        break
    else:
        print("不可以之答\n")
        round_time -= one
        continue

    answer = "儒:" + player + " 比 " + "算盤:" + computer
    print("上為果")
    time.sleep(1)
    print("")
    print("下為擇")
    print(answer)

    per = win_time / round_time * hundred
    time.sleep(3)

if player == "停" and round_time == 0:
    print("\n\n\n")
    print("猜枚戲，造作者企鵝 \n 版. 1.0.6 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("敢問高姓？： \n > > >")
    cmd("cls")
    print("儒：", name)
    print("戲回：", round_time)
    print("勝回：", win_time)
    print("勝之率：", per ,"%")
    print("\n")
    if per < 50:
        print("算盤:不如畜，易戲敗之樣，父母以儒為恥。")
    else:
        print("算盤:勝不驕，敗不餒。儒驕枉儒之勝。")


    print("\n\n\n")
    print("猜枚戲，造作者企鵝 \n 版. 1.0.6 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()