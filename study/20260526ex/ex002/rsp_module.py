import random

userNum = []
computerNum = []

def setUNumber(ns):        # setter    set + UserNum => set + UNum
    global userNum
    userNum = ns

def getUNumber():          # getter    get + UserNum => set + UNum
    return userNum

def setRNumber():        # setter    set + UserNum => set + UNum
    global computerNum
    computerNum = random.randint(0, 2)

def getRNumber():          # getter    get + UserNum => set + UNum
    return computerNum

def compareNumber():
    global userNum
    global computerNum

    if userNum == computerNum:
        print('무승부!')
    
    elif (
        (userNum == 0 and computerNum == 2) or
        (userNum == 1 and computerNum == 0) or
        (userNum == 2 and computerNum == 1)
    ):
        print('사용자 승리!')

    else:
        print('컴퓨터 승리!')



