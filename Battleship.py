#codes
import random
#opening
def printBoard():
    for i in range(rows):
        board2 = str(arr2[i])[1:-1]
        print(board2)

def printActualBoard():
    for i in range(rows):
        board = str(arr[i])[1:-1]
        print(board)

print("____________________________")
print("         Battleship         ")
print("----------------------------")
start = input("Please press enter to start")
#board base code
arr=[]
arr2=[]
rows, cols=10,10
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(".")
    arr.append(col)
    
rows2, cols2=10,10
for i in range(rows2):
    col2 = []
    for j in range(cols2):
        col2.append(".")
    arr2.append(col2)
printBoard()
#randomizer&battleship placement of CPU
xtemp = []
ytemp = []
counter = 0
while True:
    x = random.randint(0,4)
    y = random.randint(0,8)
    if x not in xtemp:
        if y not in ytemp:
            if arr[x][y+1] == ".":
                arr[x][y] = "o"
                arr[x][y+1] = "o"
                counter = counter+1
                xtemp.append(x)
                ytemp.append(y)
    if counter == 3:
        break

#battleship placement
x2temp = []
y2temp = []
counter2 = 0
while True:
    if counter2 == 3:
        print("Thanks for putting 3 battleships!")
        break
    y2 = int(input("Please input the coloum number (0-9):"))
    x2 = int(input("Please input the row number (5-9):"))
    if (int(x2) in range(5, 10) and int(y2) in range(0, 10)):
        if arr[int(x2)][int(y2)] == ".":
            arr[int(x2)][int(y2)] = ("o") #arr adalah Board yang Kelihatan Posisi Musuhnya
            arr2[int(x2)][int(y2)] = ("o") #arr2 adalah Board yang Tidak Kelihatan Posisi Musuhnya
            print("first section")
            while True:
                n = random.randint(1,4)
                if n == 1 and y2<9: #Ini Arahnya ke Kanan
                    if arr[int(x2)][int(y2)+1] == ".":
                        arr[int(x2)][int(y2)+1] = ("o")
                        arr2[int(x2)][int(y2)+1] = ("o")
                        x2temp.append(x2)
                        y2temp.append(y2)
                        print("second section")
                        counter2 = counter2+1
                        break
                    else:
                        continue                     
                if n == 2 and x2<9: #Ini Arahnya ke Bawah
                    if arr [int(x2)+1][int(y2)] == ".":
                        arr[int(x2)+1][int(y2)] = ("o")
                        arr2[int(x2)+1][int(y2)] = ("o")
                        x2temp.append(x2)
                        y2temp.append(y2)
                        print("second section")
                        counter2 = counter2+1
                        break
                    else:
                        continue                  
                if n == 3 and y2>0: #Ini Arahnya ke Kiri
                    if arr [int(x2)][int(y2)-1] == ".":
                        arr[int(x2)][int(y2)-1] = ("o")
                        arr2[int(x2)][int(y2)-1] = ("o")
                        x2temp.append(x2)
                        y2temp.append(y2)
                        print("second section")
                        counter2 = counter2+1
                        break
                    else:
                        continue                                       
                if n == 4 and x2>5: #Ini Arahnya ke Atas
                    if arr[int(x2)-1][int(y2)] == ".":
                        arr[int(x2)-1][int(y2)] = ("o")
                        arr2[int(x2)-1][int(y2)] = ("o")
                        x2temp.append(x2)
                        y2temp.append(y2)
                        print("second section")
                        counter2 = counter2+1
                        break
                    else:
                        continue
        else:
            print("You have already filled this spot!")
            continue                              
    else:
        print("The row/coloumn you enter is incorrect!")
        continue
    printBoard()
print("Attack time")
#first player
p = random.randint(1,2)
if p == 1:
    counter3=0
    counter4=0
    while True:
        print("The computer is going to start first")
        while True:
            x2 = random.randint(5,9)
            y2 = random.randint(0,9)
            if arr[x2][y2] == "o":
                arr[x2][y2] = "d"
                arr2[x2][y2] = "d"
                counter3 = counter3+1
                print("The computer has located you're battleship at row: "+str(x2)+", coloumn: "+str(y2))
            elif arr[x2][y2] == ".":
                arr[x2][y2] = "e"
                arr2[x2][y2] = "e"
                print("The computer has failed to locate any battleship at row: "+str(x2)+", coloumn: "+str(y2))
                break
            else:
                continue
        while True:
            xu = int(input("Please input the row number (0-4):"))
            yu = int(input("Please input the column number (0-9):"))
            if xu>=0 and xu<=4 and yu>=0 and yu<=9:
                if arr[xu][yu] == "o":
                    arr[xu][yu] = "d"
                    arr2[xu][yu] = "d"
                    print("You've located the enemy battleship at row: "+str(xu)+", coloumn: "+str(yu))
                    counter4 = counter3+1
                elif arr[xu][yu] == ".":
                    arr[xu][yu] = "e"
                    arr2[xu][yu] = "e"
                    print("You've failed to locate the enemy battleship at row: "+str(xu)+", coloumn: "+str(yu))
                printBoard()
                break
            else:
                print("You cannot attack this spot! Please try again")
        if counter3 == 6:
            print("You have been defeated!")
            break
        if counter4 == 6:
            print("Congratulation! You have destroyed all the enemy's battleship.")
            break
if p == 2:
    print("You're going to to start first")
    counter5=0
    counter6=0
    while True:
        while True:
            xu = int(input("Please input the row number (0-4):"))
            yu = int(input("Please input the column number (0-9):"))
            if xu>=0 and xu<=4 and yu>=0 and yu<=9:
                if arr[xu][yu] == "o":
                    arr[xu][yu] = "d"
                    arr2[xu][yu] = "d"
                    counter6 = counter6+1
                    print("You've located the enemy battleship at row: "+str(xu)+", coloumn: "+str(yu))
                elif arr[xu][yu] == ".":
                    arr[xu][yu] = "e"
                    arr2[xu][yu] = "e"
                    print("You've failed to locate the enemy battleship at row: "+str(xu)+", coloumn: "+str(yu))
                break
            else:
                print("You cannot attack this spot! Please try again")
        while True:
            x2 = random.randint(5,9)
            y2 = random.randint(0,9)
            if arr[x2][y2] == "o":
                arr[x2][y2] = "d"
                arr2[x2][y2] = "d"
                counter5 = counter5+1
                print("The computer has located you're battleship at row: "+str(x2)+", coloumn: "+str(y2))
            elif arr[x2][y2] == ".":
                arr[x2][y2] = "e"
                arr2[x2][y2] = "e"
                print("The computer has failed to locate any battleship at row: "+str(x2)+", coloumn: "+str(y2))
                printBoard()
                break
            else:
                continue
        if counter5 == 6:
            print("You have been defeated!")
            break
        if counter6 == 6:
            print("Congratulation! You have destroyed all the enemy's battleship.")
            break