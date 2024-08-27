import os
import random
import msvcrt
import time
from random import choice
from os import system as cmd

cmd("title 以緣分之組")
cmd("cls")
print("以緣分之組，造作者企鵝 \n 版. 1.0.1 勿改 \n\n\n")
print("一彈指，即始。")
time.sleep(5)
cmd("cls")

while True:
    input_players = ""
    while not input_players.strip():
        input_players = input("告眾之名，以「、」分之，或以停為止。\n(例:孔子、李白、杜甫) \n > > >")
    if input_players == "stop":
        break
    else:
        input_players = input_players.split('、')

    input_team = ""
    while not input_team.strip():
        input_team = input("告組之名，以「、」分之。\n (例:文士組、農民組、商賈組。) \n > > > ")
    input_team = input_team.split("、")

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
                print(f'{teams[team_key]} 之員: {", ".join(T_list[index])}')
                time.sleep(0.3)

        while True:
            ans = input("重新以緣分之?(是/否) \n > > >")
            if ans == "是":
                print("以緣分之組中")
                cmd("cls")
                break
            elif ans == "否":
                print()
                while True:
                    ans_2 = input("復始以緣分之(復)，亦以之為組(許) \n (註: 復始亦重始以緣分之，以為組即存之。) \n > > > ")
                    if ans_2 == "復":
                        print()
                        break
                    elif ans_2 == "許":
                        print()
                        break
                    else:
                        print("不可以之答")
                        continue
                if ans_2 == "復":
                    print()
                    break
                elif ans_2 == "許":
                    print()
                    break
            elif ans == "":
                continue
            else:
                print("不可以之答")
                continue                       

            if ans_2 == "復":
                print("除答之")        
                time.sleep(3)
                break  
            elif ans_2 == "許":
                print("存答之")
                time.sleep(2)
                break 
        
        if ans == "是":
            continue
        if ans_2 == "復":
            cmd("cls")
            break
        elif ans_2 == "許":
            print()
            break
    if ans_2 == "復":
        cmd("cls")
        continue
    elif ans_2 == "許":
        print()
        break                 

if input_players == "停":
    cmd("cls")
    print("以緣分之組，造作者企鵝 \n 版. 1.0.1 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()
else:
    print()
    cmd("cls")
    for index, team_key in enumerate(teams.keys()):
        if index < len(T_list):
            print(f'{teams[team_key]} 之員: {", ".join(T_list[index])}')
            time.sleep(0.2)

    print("\n\n")
    print("以緣分之組，造作者企鵝 \n 版. 1.0.1 勿改")
    print("\n\n\n擇一鈕以離亦閉之")
    msvcrt.getch()