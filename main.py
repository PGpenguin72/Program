import time
import subprocess
import os 
from os import system as cmd

location = os.path.dirname(__file__)
Games = os.path.join(location, "Games")

cmd("cls")
print("小遊戲大集結，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")
print("目前擁有的程序:")

for dirpath, dirnames, filenames in os.walk(Games):
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        print(">", name)
    
Uinput = input("請問你想玩什麼遊戲?")
if Uinput == "猜拳":
    os.chdir(Games)
    cmd("cls")
    cmd("python 猜拳.py")
elif Uinput == "賽龜":
    os.chdir(Games)
    cmd("cls")
    cmd("python 賽龜.py")
else:
    print("目前不支持此軟件，請重新啟動main.py")