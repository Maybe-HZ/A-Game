import os
import random
from time import sleep
import sys
import turtle

def exit(exit):
    os._exit(1)

def inGame2(x):
    if x == True:
        txt1 =("Dengan status kekuatanmu saat ini kamu bisa disebut")
        txt2 =("Berhati-hatilah dalam berpetualang diluar sana")
        
    print("====================================================================")
    for x in txt1:
        for y in x:
            print(y,end='')
            sys.stdout.flush()
            sleep(0.01)
        print(end="")
    print(" ",end="")
    for x in statusku:
        for y in x:
            print(y,end='')
            sys.stdout.flush()
            sleep(0.01)
        print(end="")
    print("")
    for x in txt2:
        for y in x:
            print(y,end='')
            sys.stdout.flush()
            sleep(0.01)
        print(end="")
    print("")    
    print("====================================================================")
    exit(True)
        
def gachaStatus(x):
    global statusku
    global status
    if x == True:
        status = random.randint(0,100)
        if status <= 15:
            statusku = "Wibu Anti sosial Yang Lemah"
        elif status > 15 and status <= 24:
            statusku = "Manusia Dibawah rata\""
        elif status == 25:
            statusku = "Manusia normal"
        elif status > 25 and status <= 50:
            statusku = "SuperHuman"
        elif status > 50 and status <= 75:
            statusku = "SuperHuman High Rank"
        elif status > 75:
            statusku = "Undefeatable between Human"
        print(status)
        inGame2(True)
    elif x == False:
        status = 25
        statusku = "Manusia normal"
        print(status)
        inGame2(True)
    return statusku,status

def inGame1(x):
    def reAsk():
        input1 = input("Apakah kamu ingin menggacha statusmu [y/n] : ")
        if input1 == 'y':
            gachaStatus(True)
        elif input1 == 'n':
            gachaStatus(False)
        else:
            reAsk()
            
    if x == True:
        txt1=[  "> Disini kamu akan bermain sebagai seorang aldo",
                "> Petualanganmu akan dimulai dari sebuah desa",
                "> Tujuan petualanganmu adalah untuk mencari seorang wanita impian"]

        print("======================================================================")
        for x in txt1:
            for y in x:
                print(y,end='')
                sys.stdout.flush()
                sleep(0.01)
            print(" ")
        print("======================================================================")
        input1 = input("Apakah kamu ingin menggacha statusmu [y/n] : ")
        if input1 == 'y':
            gachaStatus(True)
        elif input1 == 'n':
            gachaStatus(False)
        else:
            reAsk()
            
def playSelectRage(x):
    if x == True:
        print("KELUAR PEPEK !!!!!!")
        turtle.speed(7)
        turtle.begin_fill()
        turtle.circle(100,450)
        turtle.right(100)
        turtle.right(80)
        turtle.circle(100,625)
        turtle.right(85)
        turtle.forward(425)
        turtle.circle(100,175)
        turtle.left(5)
        turtle.forward(450)
        turtle.end_fill()
        turtle.done()
        os._exit(1)

def playSelect(txtInput):
    if txtInput == 0:
        os.system('cls')
        os._exit(1)
    elif txtInput == 1:
        os.system("cls")
        inGame1(True)
    else:
        os.system("cls")
        txtInput = int(input("Choose only between [1/0] : "))
        if txtInput == 0:
            os._exit(1)
        elif txtInput == 1:
            inGame1(True)
        else:
            playSelectRage(True)    


print(  "   /\\   |      |‾\\   |‾‾‾‾|")
print(  "  /  \\  |      |  \\  |    |")
print(  " /____\\ |      |  /  |    |")
print(  "/      \\|_____ |_/   |____|   Adventure")
print("")
txtInput = int(input("Wanna Play [0/1] :"))
if txtInput == 0:
    playSelect(0)
elif txtInput == 1:
    playSelect(1)
    inGame1(True)
else:
    playSelect(" ")


    