import random
import os
import turtle

def TruthOrDare():
    def game(a):
        if a == True:
            y = random.sample(player, k=2)
            print("==========================================")
            print("Instrumen Ilahi : ", y[0])
            print("Pendosa         : ", y[1])
            punishment = ["Truth", "Dare"]
            punish = random.sample(punishment, k=1)
            print(" ")
            print("Wahai",y[1],"Kamu akan disucikan oleh",y[0],"dengan ", punish[0])
            print("==========================================")
            print("")

            z = input("Apakah kamu ingin menentukan ulang (y/n) :")
            print(" ")
            if z == "y":
                os.system("cls")
                game(True)
            else:
                z = input("Ingin Kembali ke main menu [y/n]")
                if z == "y":
                    os.system("cls")
                    mainMenu()
                else:
                    TruthOrDare()
    def inputPlayer():
        x = int(input("Jumlah Pemain : "))
        if x == 1:
            print("Input Selain 1 bang")
            inputPlayer()
        for i in range(x):
            plr = input("Masukkan Nama Pemain : ")
            player.append(plr)
        return player
    player = []
    inputPlayer()
    print(" ")
    z = input("Apakah kamu ingin bermain (y/n) :")
    print(" ")
    if z == "y":
        os.system("cls")
        game(True)
    else:
        mainMenu()    


def menuSelect(value):
    if value == 1:
        TruthOrDare()
    elif value == 2:
        os._exit(1)
    
        
def mainMenu():
    print("======================================================")
    print("< < < < < < Selamat Datang Dalam Permainan > > > > > >")
    print("")
    print("< < < < < < < < < < <  List Game > > > > > > > > > > >")
    print("[1] Truth or Dare")
    print("[2] Exit")
    print("======================================================")
    menuSelector = int(input("    Pilih [1/2] :"))
    os.system("cls")
    menuSelect(menuSelector)

mainMenu()
    