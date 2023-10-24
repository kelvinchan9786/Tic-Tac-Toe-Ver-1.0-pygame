from itertools import combinations

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
            

        
winninglist = [{1, 2, 3}, {4, 5 ,6}, {7 ,8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
chara = ["O", "X"]
first, second = None, None
firstpos = set()
secondpos = set()
move = 0
winset = set()
temp1, temp2 = None, None

#choose first character

first = input("Who is the first character? (O, X)") #input
if first == "O":
    second = "X"
else:
    second = "O"

#choose second character

#move
currentstep = first
while move < 9:
    while (temp1 == None) or (temp1 != None) and (temp1 in firstpos or temp1 in secondpos):
        temp1 = int(input(currentstep + ": What's your move?")) # replace this by triggering a blank image
    if currentstep == first:
        firstpos.add(temp1)
        currentstep = second
    else:
        secondpos.add(temp1)
        currentstep = first
    firstcheck = checkwin(firstpos)
    secondcheck = checkwin(secondpos)
    if  firstcheck == True or secondcheck == True:
        break
    move += 1

if firstcheck == True:
    print(first + " wins")
elif secondcheck == True:
    print(second + "wins")
else:
    print("Draw")

