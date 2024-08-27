import os
import random
import msvcrt
import time
from random import choice
from os import system as cmd

cmd("title Random Grouping")
cmd("cls")
print("Random Grouping, Made By.PGpenguin72 \n ver. 1.0.1 Do not modify the code arbitrarily. \n\n\n")
print("(Start grouping in 3 seconds!)")
time.sleep(3)
cmd("cls")

while True:
    input_players = ""
    while not input_players.strip():
        input_players = input('Enter the member list, and separate every member's name with ", " (or enter "stop" to end grouping.) \n(e.g. John, Mandy, Jason... etc.) \n > > >')
    if input_players == "stop":
        break
    else:
        input_players = input_players.split(', ')

    input_team = ""
    while not input_team.strip():
        input_team = input('Enter team names, and separate every team name with "," (26 teams at most.) \n (e.g. Penguin, Crab, Polar Bear... etc.) \n > > > ')
    input_team = input_team.split(", ")

    team_Raw = input_team
    player_raw = input_players

    while True:

        input_team = team_Raw
        input_players = player_raw

        teams = {}

        fountion = 1 

        for t in input_team:
            key = f'team_{fountion}'
            teams[key] = t
            fountion += 1

        T_fountion = fountion -1 #隊伍總數

        players = {}
        fountion = 1

        for p in input_players:
            player = f'player_{fountion}'
            players[player] = p
            fountion += 1

        P_list = list(players.values())
        T_list = [[] for _ in range(T_fountion)]

        fountion -= 1
        P_fountion = fountion
        fountion = 1

        while len(P_list) > 0:
            for i in range(T_fountion):
                if P_list:
                    player = choice(P_list)
                    T_list[i].append(player)
                    P_list.remove(player)

        print()
        cmd("cls")
        for index, team_key in enumerate(teams.keys()):
            if index < len(T_list):
                print(f'{teams[team_key]} member: {", ".join(T_list[index])}')
                time.sleep(0.3)

        while True:
            ans = input("Regroup or not?(Y/N) \n > > >")
            if ans == "Y":
                print("Regroup preparing...")
                cmd("cls")
                break
            elif ans == "N":
                print()
                while True:
                    ans_2 = input("Resume(R) or Calculate (C)? \n (Note: resume to delete all data; calculate to save grouping result in terminal.) \n > > > ")
                    if ans_2 == "R":
                        print()
                        break
                    elif ans_2 == "C":
                        print()
                        break
                    else:
                        print("Please check your text.")
                        continue
                if ans_2 == "R":
                    print()
                    break
                elif ans_2 == "C":
                    print()
                    break
            elif ans == "":
                continue
            else:
                print("Please check your text.")
                continue                       

            if ans_2 == "R":
                print("Data deleting...")        
                time.sleep(3)
                break  
            elif ans_2 == "C":
                print("Data recording...")
                time.sleep(2)
                break 
        
        if ans == "Y":
            continue
        elif ans_2 == "R":
            cmd("cls")
            break
        elif ans_2 == "C":
            print()
            break
    if ans_2 == "R":
        cmd("cls")
        continue
    elif ans_2 == "C":
        print()
        break                 

if input_players == "stop":
    cmd("cls")
    print("Random Grouping, Made By.PGpenguin72 \n ver. 1.0.1 Do not modify the code arbitrarily. \n\n\n")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()
else:
    print()
    cmd("cls")
    for index, team_key in enumerate(teams.keys()):
        if index < len(T_list):
            print(f'{teams[team_key]} member: {", ".join(T_list[index])}')
            time.sleep(0.2)

    print("\n\n")
    print("Random Grouping, Made By.PGpenguin72 \n ver. 1.0.1 Do not modify the code arbitrarily. \n\n\n")
    print("\n\n\nPress any key to exit or close the program.")
    msvcrt.getch()