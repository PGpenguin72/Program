import time
import subprocess
import os 
from os import system as cmd

program = "/program/"

print("小遊戲大集結，Made By.PGpenguin72 \n ver. 1.0.4 請勿隨意修改程序碼")
print("目前擁有的程序:")
for dirpath, dirnames, filenames in os.walk(program):
    for filename in filenames:
        print(filename)
