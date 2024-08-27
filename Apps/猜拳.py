import random
import time
import msvcrt
import json
import os
from os import system as cmd

cmd("title Paper-Scissors-Stone")
print("Paper-Scissors-Stone, Made By.PGpenguin72 \n ver. 1.0.6 Do not modify the code arbitrarily")
print("Game starts in 3 seconds!")

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
    print("Round Time:", round_time)
    print("Win Time:", win_time)
    print("Winning Rate:", per ,"%")
    print("++++++++++++++++++++++++++")
    round_time += one
    print("Round", round_time)
    player = input("choose paper, scissors, or stone (or enter "stop" to calculate score) \n > > >")
    computer = random.choice(["Paper", "Scissors", "Stone"])
    print("\n")
    W = "You win\n"
    L = "You lose\n\n"
    
    if player == computer:
        print("Draw \n")
        win_time += half
    elif player == "Scissors":
        if computer == "Paper":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "Stone":
        if computer == "Scissors":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "Paper":
        if computer == "Stone":
            print(W)
            win_time += one
        else:
            print(L)
    elif player == "stop":
        round_time -= one
        break
    else:
        print("ERROR (invalid answer)\n")
        round_time -= one
        continue

    answer = "Player:" + player + "Vs. " + "Computer:" + computer
    print("Match result on the upper side")
    time.sleep(1)
    print("")
    print("choice of each side on the lower side")
    print(answer)

    per = win_time / round_time * hundred
    time.sleep(3)

if player == "stop" and round_time == 0:
    print("\n\n\n")
    print("Paper-Scissors-Stone, Made By.PGpenguin72 \n ver. 1.0.6 Do not modify the code arbitrarily.")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()
else:
    print("\n\n\n")
    name = input("please enter your name: \n > > >")
    cmd("cls")
    print("Name:", name)
    print("Round time:", round_time)
    print("Win time:", win_time)
    print("Winning rate:", per ,"%")
    print("\n")
    if per < 50:
        print("System:Ha ha, you suck! Come on! Don't be such a sore loser. (just kidding)")
    else:
        print("System:Yeah, yeah. Aren't you great. (just kidding)")


    print("\n\n\n")
    print("Paper-Scissors-Stone, Made By.PGpenguin72 \n ver. 1.0.6 Do not modify the code arbitrarily.")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()