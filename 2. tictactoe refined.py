from itertools import combinations
import pygame

def switchchara(temp01):
    if temp01 == "O":
        return "X"
    else:
        return "O"

def checkwin(temp02):
    temp020= set()
    if len(temp02) < 3:
        return False
    else:
        temp021 = list(combinations(temp02, 3))
        for temp022 in temp021:
            temp023 = set(temp022)
            if temp023 in winninglist:
                return True
                break
            else:
                temp020 = set()
                return False
            
def choosechara(temp03):
    if temp03 == "O":
        return ("O", "X")
    else:
        return ("X", "O")

def changechara(temp04):
    if currentstep == first:
        firstpos.add(temp1)
        return second
    if currentstep == second:
        secondpos.add(temp1)
        return first
        
winninglist = [{1, 2, 3}, {4, 5 ,6}, {7 ,8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
chara = ["O", "X"]
first, second = None, None
firstpos = set()
secondpos = set()
move = 0
win = None
winset = set()
temp1, temp2 = None, None

def choosemove():
    while (temp1 == None) or (temp1 != None) and (temp1 in firstpos or temp1 in secondpos):
        return int(input(currentstep + ": What's your move?")) # replace this by triggering a blank image


def changeplayer(temp05):
    if temp05 == first:
        firstpos.add(temp1)
        return second
    else:
        secondpos.add(temp1)
        return first

def winningdisplay(temp061, temp062):
    if firstcheck == True:
        return 1
    if secondcheck == True:
        return 2
    else:
        return 3 
       
inputchara = choosechara(input("Who is the first character? (O, X)"))
first = inputchara[0]
second = inputchara[1]

#start from Line 54 in original programme
currentstep = first
while (win == None) and move < 9:
    temp1 = choosemove()
    currentstep = changeplayer(currentstep)
    firstcheck = checkwin(firstpos)
    secondcheck = checkwin(secondpos)
    if firstcheck == True or secondcheck == True:
        break
    move += 1

winningdisplayvar = winningdisplay(firstcheck, secondcheck)

    
    
















