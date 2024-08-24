import time
import subprocess
import os 
from os import system as cmd

location = os.path.dirname(__file__)
Games = os.path.join(location, "Apps")

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
        cmd("python 猜拳.py")
        break
    elif Uinput == "賽龜":
        os.chdir(Games)
        print("\n\n\n 正在啟動小程序:D")
        time.sleep(3)
        cmd("cls")
        cmd("python 賽龜.py")
        break
    elif Uinput == "隨機分組":
        os.chdir(Games)
        print("\n\n\n 正在啟動小程序:D")
        time.sleep(3)
        cmd("cls")
        cmd("python 隨機分組.py")
        break
    else:
        print("\n\n\n (目前不支持此軟件，請重新輸入)")
        time.sleep(3)
        continue