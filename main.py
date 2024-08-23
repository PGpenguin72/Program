import random
import time
import msvcrt
from os import system as cmd

print("猜拳小程式，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")
print("3秒後即將開始遊戲！")

win_time = int(0)
round_time = int(0)
half = 0.5
one = 1
hundred = 100
per = 100

cmd("title 猜拳小程序")

time.sleep(3)

while True:
    cmd("cls")

    round_time = round_time + one
    print("++++++++++++++++++++++++++")
    print("目前局數：", round_time)
    print("贏的局數：", win_time)
    print("勝率：", per ,"%")
    print("++++++++++++++++++++++++++")

    player = input("選擇你要出剪刀,石頭,還是布? (或輸入stop來結算成績) \n > > >")
    computer = random.choice(["剪刀", "石頭", "布"])
    print("\n")
    
    W = "你贏了\n"
    L = "你輸了\n\n"

    if(player == computer):
        print("平局 \n")
        win_time = win_time + half

    else:
        if(player == "剪刀"):
            if(computer == "布"):
                print(W)
                win_time = win_time + one
            else:
                print(L)
        else:
            if(player == "石頭"):
                if(computer == "剪刀"):
                    print(W)
                    win_time = win_time + one
                else:
                    print(L)
            else:
                if(player == "布"):
                    if(computer == "石頭"):
                        print(W)
                        win_time = win_time + one
                    else:
                        print(L)
                else:
                    if(player == "stop"):
                        round_time = round_time - one
                        break
                    else:
                        print("ERROR(無效回答)\n")
                        round_time = round_time - one

    answer = "玩家:" + player + " Vs. " + "電腦:" + computer
    print("上面是對戰結果")
    time.sleep(1)
    print("")
    print("下面是雙方的選擇")

    print(answer)
    
    if(round_time == 0):
        print("請重新開始")
        break
    else:
        per = win_time / round_time * hundred
    
    time.sleep(3)

if(round_time == 0):
    print("=========================================")
    print("錯誤訊息：'局數=0，無法計算，操作請慢一點。'")
    print("=========================================")
else:
    print("\n\n\n\n （往下滑繼續） \n\n\n\n\n")
    name = input("請輸入你的名字： \n > > >")
    cmd("cls")
    print("姓名：", name)
    print("遊玩局數：", round_time)
    print("贏的局數：", win_time)
    print("勝率：", per ,"%")
    print("\n\n\n")
    if(per < 50):
        print("System:蔡，就多練！輸不起就別玩（誤")
    else:
        print("System:好哦好哦，阿不就好棒棒（誤")
    print()
    print("猜拳小程式，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")

print("\n\n\n\n按下任意鍵離開或關閉程序")
msvcrt.getch()
