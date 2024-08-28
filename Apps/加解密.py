import random
import time
import msvcrt
import os
import base64
from os import system as cmd

cmd("title 加解密小程序")
print("加解密小程序，Made By.PGpenguin72 \n ver. 1.0.0 請勿隨意修改程序碼")
print("3秒後即將開始！")
time.sleep(3)
cmd("cls")

#加密用
basePG = {
    "1": "PGOW57",
    "2": "PGjS84",
    "3": "PGxo65",
    "4": "PGaj72",
    "5": "PGOH04",
    "6": "PGrg46",
    "7": "PGsq40",
    "8": "PGAl50",
    "9": "PGuH62",
    "0": "PGkN71",
    "Q": "PGse24",
    "W": "PGSs35",
    "E": "PGsd32",
    "R": "PGMG03",
    "T": "PGPX81",
    "Y": "PGzq10",
    "U": "PGgU61",
    "I": "PGkJ04",
    "O": "PGvW01",
    "P": "PGQo70",
    "A": "PGwf25",
    "S": "PGuX17",
    "D": "PGyQ52",
    "F": "PGbz05",
    "G": "PGWF76",
    "H": "PGVK19",
    "J": "PGuq41",
    "K": "PGqS93",
    "L": "PGRN28",
    "Z": "PGZh47",
    "X": "PGlp90",
    "C": "PGeG26",
    "V": "PGlU85",
    "B": "PGvi93",
    "N": "PGZU03",
    "M": "PGqG36",
    "q": "PGpj78",
    "w": "PGmD60",
    "e": "PGGP52",
    "r": "PGwu40",
    "t": "PGaf82",
    "y": "PGMh48",
    "u": "PGlT26",
    "i": "PGtd61",
    "o": "PGwI59",
    "p": "PGfq60",
    "a": "PGbe04",
    "s": "PGmA94",
    "d": "PGZn69",
    "f": "PGKj50",
    "g": "PGqW79",
    "h": "PGXC89",
    "j": "PGWr78",
    "k": "PGYs02",
    "l": "PGjW32",
    "z": "PGOe21",
    "x": "PGGF15",
    "c": "PGBE01",
    "v": "PGCU28",
    "b": "PGiF48",
    "n": "PGOD46",
    "m": "PGtk71"
}
caser = {
    '1': '4',
    '2': '5',
    '3': '6',
    '4': '7',
    '5': '8',
    '6': '9',
    '7': '0',
    '8': '1',
    '9': '2',
    '0': '3',
    'Q': 'T',
    'W': 'Z',
    'E': 'H',
    'R': 'U',
    'T': 'W',
    'Y': 'B',
    'U': 'X',
    'I': 'L',
    'O': 'R',
    'P': 'S',
    'A': 'D',
    'S': 'V',
    'D': 'G',
    'F': 'I',
    'G': 'K',
    'H': 'M',
    'J': 'N',
    'K': 'O',
    'L': 'C',
    'Z': 'Y',
    'X': 'E',
    'C': 'F',
    'V': 'K',
    'B': 'o',
    'N': 't',
    'M': 'h',
    'q': 'u',
    'w': 'x',
    'e': '1',
    'r': 'l',
    't': 'v',
    'y': 'i',
    'u': 'm',
    'i': 'p',
    'o': 'b',
    'p': 'g',
    'a': 'm',
    's': 'o',
    'd': 'q',
    'f': 'r',
    'g': 'v',
    'h': 'c',
    'j': 'w',
    'k': 'f',
    'l': 'd',
    'z': 'y',
    'x': 'e',
    'c': 'j',
    'v': 'p',
    'b': 'k',
    'n': 'o',
    'm': 'q'
}
morse = {
    '1': '· - - - -',
    '2': '· · - - -',
    '3': '· · · - -',
    '4': '· · · · -',
    '5': '· · · · ·',
    '6': '- · · · ·',
    '7': '- - · · ·',
    '8': '- - - · ·',
    '9': '- - - - ·',
    '0': '- - - - -',
    'Q': '- - · - ·',
    'W': '· - -',
    'E': '·',
    'R': '· - ·',
    'T': '-',
    'Y': '- · - -',
    'U': '· · -',
    'I': '· ·',
    'O': '- - -',
    'P': '· - - ·',
    'A': '· -',
    'S': '· · ·',
    'D': '- · ·',
    'F': '· · - ·',
    'G': '- - ·',
    'H': '· · · ·',
    'J': '· - - -',
    'K': '- · -',
    'L': '· - · ·',
    'Z': '- - · ·',
    'X': '- · · -',
    'C': '- · - ·',
    'V': '· · · -',
    'B': '- · · ·',
    'N': '- ·',
    'M': '- -',
    'q': '- - · - ·',
    'w': '· - -',
    'e': '·',
    'r': '· - ·',
    't': '-',
    'y': '- · - -',
    'u': '· · -',
    'i': '· ·',
    'o': '- - -',
    'p': '· - - ·',
    'a': '· -',
    's': '· · ·',
    'd': '- · ·',
    'f': '· · - ·',
    'g': '- - ·',
    'h': '· · · ·',
    'j': '· - - -',
    'k': '- · -',
    'l': '· - · ·',
    'z': '- - · ·',
    'x': '- · · -',
    'c': '- · - ·',
    'v': '· · · -',
    'b': '- · · ·',
    'n': '- ·',
    'm': '- -'
}
#解密用
basePG_Raw ={
    "PGOW57": "1",
    "PGjS84": "2",
    "PGxo65": "3",
    "PGaj72": "4",
    "PGOH04": "5",
    "PGrg46": "6",
    "PGsq40": "7",
    "PGAl50": "8",
    "PGuH62": "9",
    "PGkN71": "0",
    "PGse24": "Q",
    "PGSs35": "W",
    "PGsd32": "E",
    "PGMG03": "R",
    "PGPX81": "T",
    "PGzq10": "Y",
    "PGgU61": "U",
    "PGkJ04": "I",
    "PGvW01": "O",
    "PGQo70": "P",
    "PGwf25": "A",
    "PGuX17": "S",
    "PGyQ52": "D",
    "PGbz05": "F",
    "PGWF76": "G",
    "PGVK19": "H",
    "PGuq41": "J",
    "PGqS93": "K",
    "PGRN28": "L",
    "PGZh47": "Z",
    "PGlp90": "X",
    "PGeG26": "C",
    "PGlU85": "V",
    "PGvi93": "B",
    "PGZU03": "N",
    "PGqG36": "M",
    "PGpj78": "q",
    "PGmD60": "w",
    "PGGP52": "e",
    "PGwu40": "r",
    "PGaf82": "t",
    "PGMh48": "y",
    "PGlT26": "u",
    "PGtd61": "i",
    "PGwI59": "o",
    "PGfq60": "p",
    "PGbe04": "a",
    "PGmA94": "s",
    "PGZn69": "d",
    "PGKj50": "f",
    "PGqW79": "g",
    "PGXC89": "h",
    "PGWr78": "j",
    "PGYs02": "k",
    "PGjW32": "l",
    "PGOe21": "z",
    "PGGF15": "x",
    "PGBE01": "c",
    "PGCU28": "v",
    "PGiF48": "b",
    "PGOD46": "n",
    "PGtk71": "m"
}
caser_Raw ={
    '4': '1',
    '5': '2',
    '6': '3',
    '7': '4',
    '8': '5',
    '9': '6',
    '0': '7',
    '1': '8',
    '2': '9',
    '3': '0',
    'T': 'Q',
    'Z': 'W',
    'H': 'E',
    'U': 'R',
    'W': 'T',
    'B': 'Y',
    'X': 'U',
    'L': 'I',
    'R': 'O',
    'S': 'P',
    'D': 'A',
    'V': 'S',
    'G': 'D',
    'I': 'F',
    'K': 'G',
    'M': 'H',
    'N': 'J',
    'O': 'K',
    'C': 'L',
    'Y': 'Z',
    'E': 'X',
    'F': 'C',
    'K': 'V',
    'o': 'B',
    't': 'N',
    'h': 'M',
    'u': 'q',
    'x': 'w',
    '1': 'e',
    'l': 'r',
    'v': 't',
    'i': 'y',
    'm': 'u',
    'p': 'i',
    'b': 'o',
    'g': 'p',
    'm': 'a',
    'o': 's',
    'q': 'd',
    'r': 'f',
    'v': 'g',
    'c': 'h',
    'w': 'j',
    'f': 'k',
    'd': 'l',
    'y': 'z',
    'e': 'x',
    'j': 'c',
    'p': 'v',
    'k': 'b',
    'o': 'n',
    'q': 'm'
}
morse_Raw = {
    '· - - - -': '1',
    '· · - - -': '2',
    '· · · - -': '3',
    '· · · · -': '4',
    '· · · · ·': '5',
    '- · · · ·': '6',
    '- - · · ·': '7',
    '- - - · ·': '8',
    '- - - - ·': '9',
    '- - - - -': '0',
    '- - · - ·': 'Q',
    '· - -': 'W',
    '·': 'E',
    '· - ·': 'R',
    '-': 'T',
    '- · - -': 'Y',
    '· · -': 'U',
    '· ·': 'I',
    '- - -': 'O',
    '· - - ·': 'P',
    '· -': 'A',
    '· · ·': 'S',
    '- · ·': 'D',
    '· · - ·': 'F',
    '- - ·': 'G',
    '· · · ·': 'H',
    '· - - -': 'J',
    '- · -': 'K',
    '· - · ·': 'L',
    '- - · ·': 'Z',
    '- · · -': 'X',
    '- · - ·': 'C',
    '· · · -': 'V',
    '- · · ·': 'B',
    '- ·': 'N',
    '- -': 'M',
    '- - · - ·': 'q',
    '· - -': 'w',
    '·': 'e',
    '· - ·': 'r',
    '-': 't',
    '- · - -': 'y',
    '· · -': 'u',
    '· ·': 'i',
    '- - -': 'o',
    '· - - ·': 'p',
    '· -': 'a',
    '· · ·': 's',
    '- · ·': 'd',
    '· · - ·': 'f',
    '- - ·': 'g',
    '· · · ·': 'h',
    '· - - -': 'j',
    '- · -': 'k',
    '· - · ·': 'l',
    '- - · ·': 'z',
    '- · · -': 'x',
    '- · - ·': 'c',
    '· · · -': 'v',
    '- · · ·': 'b',
    '- ·': 'n',
    '- -': 'm'
}
while True:
    while True:
        print("目前支持的加密方式:\n base64 \n basePG--只支持英文及數字 \n 凱薩加密--只支持英文及數字 \n 摩斯密碼--只支持英文及數字 \n\n")#(base64 , basePG, caesar cipher, morse code)
        Uinput = input("請選擇你要加密(E)還是解密(D):\n > > > ")
        if Uinput == "E":
            print("(若程序崩潰表輸入內容無法成功編碼，請刪除空格或其他字元，並重新啟動程序。)")
            text = input("請輸入你要編碼的文字:\n > > > ")
            print("\n\n編碼中")
            time.sleep(3)
            text_A = text.encode('UTF-8')
            answer_A = base64.b64encode(text_A)
            answer_A = answer_A.decode('UTF-8').replace("b", "").replace("'", "").replace("=", "")
            text_B = list(text)
            answer_B = ""
            fountion = 0
            for char in text:
                if char in basePG:
                    first = text_B[fountion]
                    answer_vir = basePG[first]
                    answer_B += answer_vir
                    fountion += 1
                else:
                    answer_B = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            text_C = list(text)
            answer_C = ""            
            fountion = 0
            for char in text:
                if char in caser:
                    first = text_C[fountion]
                    answer_vir = caser[first]
                    answer_C += answer_vir
                    fountion += 1
                else:
                    answer_C = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            text_D = list(text)
            answer_D = ""
            fountion = 0
            for char in text:
                if char in morse:
                    first = text_D[fountion]
                    answer_vir = morse[first]
                    answer_D += answer_vir
                    answer_D += "/"
                    fountion += 1
                else:
                    answer_D = "ERROR 無法加密，請確認是否有錯誤的字元或空格。"
            cmd("cls")
            print(text, "為原文\n\n")
            print("Base64\n", answer_A)
            print("BasePG\n", answer_B)
            print("凱薩加密\n",answer_C)
            print("摩斯密碼\n",answer_D)
            break

        elif Uinput == "D":
            print("(若程序崩潰表輸入內容無法解碼，請確認輸入內容開頭沒有包含空格，並重新啟動程序。)")
            text = input("請輸入你要解碼的亂碼: \n > > > ")
            BOJI = input('請輸入解碼方式"base64(B), basePG(P), 凱薩加密(C), 摩斯密碼(M)":\n > > > ')
            print("\n\n解碼中")
            time.sleep(3)
            if BOJI == "B":
                text_A = text.encode('UTF-8')
                answer_A = base64.b64decode(text_A)
                answer_A = answer_A.decode('UTF-8').replace("b", "").replace("'", "").replace("=", "")
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_A)
            elif BOJI == "P":
                text_B_Raw = text
                six = 6
                text_B = []
                for i in range(0, len(text_B_Raw), six):
                    chunk = text_B_Raw[i:i + six]
                    text_B.append(chunk)
                fountion = 0
                answer_B_Raw = []
                for char in text_B:
                    if char in basePG_Raw:
                        first = text_B[fountion]
                        answer_vir = basePG_Raw[first]
                        answer_B_Raw += answer_vir
                        fountion += 1
                    else:
                        answer_B_Raw = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                answer_B = "".join(answer_B_Raw)
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_B)
            elif BOJI == "C":
                text_C = list(text)
                answer_C = ""            
                fountion = 0
                for char in text:
                    if char in caser_Raw:
                        first = text_C[fountion]
                        answer_vir = caser_Raw[first]
                        answer_C += answer_vir
                        fountion += 1
                    else:
                        answer_C = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                cmd("cls")
                print(text, "為原文\n\n")
                print(answer_C)
            elif BOJI == "M":
                text_D = text.split("/")
                if text_D[-1] == "":
                    text_D.pop()
                fountion = 0
                answer_D = ""
                for char in text_D:
                    if char in morse_Raw:
                        first = text_D[fountion]
                        answer_vir = morse_Raw[first]
                        answer_D += answer_vir
                        fountion += 1
                    else:
                        answer_D = "ERROR 無法解密，請確認是否有錯誤的字元或空格。"
                cmd("cls")
                print(text, "為原文\n\n")     
                print(answer_D)
            break
        elif Uinput == "stop":
            print()
        else:
            print("請確認輸入的內容。")
            time.sleep(3)
            cmd("cls")
            continue
    
    while True:
        print()
        Uinput = input("是否重新開始加密或解密?(Y/N)")
        if Uinput == "Y":
            print("請稍後")
            time.sleep(3)
            break
        elif Uinput == "N":
            print("請稍後")
            time.sleep(3)
            break
        else:
            print("請檢查輸入的內容。")
            time.sleep(3)
            continue
    if Uinput == "Y":
        print()
        cmd("cls")
        continue
    elif Uinput == "N":
        print()
        cmd("cls")
        break
        
print(text, "為原文\n\n")
print("Base64:\n", answer_A)
print("BasePG:\n", answer_B)
print("凱薩加密:\n",answer_C)
print("摩斯密碼:\n",answer_D)

print("\n\n\n加解密小程序，Made By.PGpenguin72 \n ver. 1.0.0 請勿隨意修改程序碼")
print("\n\n\n按下任意鍵離開或關閉程序")
msvcrt.getch()