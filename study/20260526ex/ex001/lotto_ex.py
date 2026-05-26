import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):        # setter    set + UserNums => set + UNums
    global userNums
    userNums = ns

def getUNumbers():          # getter    get + UserNums => set + UNums
    return userNums

def setRNumbers():        # setter    set + UserNums => set + UNums
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRNumbers():          # getter    get + UserNums => set + UNums
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(1) != 0:
            collect.append(item)

    return collect