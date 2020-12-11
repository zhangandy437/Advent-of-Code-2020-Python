def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def getSeatID(s, r = 127, c = 7):
    lr = 0
    lc = 0
    for i in s:
        if i == 'F':
            r = int((r + lr) / 2)
        if i == 'B':
            lr = int((r + lr) / 2)
        if i == 'L':
            c = int((c + lc) / 2)
        if i == 'R':
            lc = int((c + lc) / 2)
    return r * 8 + c

def getHighest(arr):
    top = 0
    for i in arr:
        cur = getSeatID(i)
        if cur > top:
            top = cur
    return top

def sumTo(n):
    return int(n * (n + 1) / 2)

def findSeat(arr, r = 127, c = 7):
    bot = r * 8
    top = 0
    total = 0
    for i in arr:
        cur = getSeatID(i, r, c)
        if cur > top:
            top = cur
        if cur < bot:
            bot = cur
        total += cur
        
    return sumTo(top) - sumTo(bot - 1) - total

print(findSeat(input("Day5/input.txt")))