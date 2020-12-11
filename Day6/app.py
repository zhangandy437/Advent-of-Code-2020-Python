def input(path):
    f = open(path, "r")
    lines = f.read().split("\n\n")
    f.close()
    return lines

def count(arr):
    c = 0
    for i in arr:
        s = set()
        for j in i:
            if j != "\n":
                s.add(j)
        c += len(s)
    return c

def everyYes(arr):
    c = 0
    for i in arr:
        d = {}
        split = i.splitlines()
        for j in split:
            for k in j:
                if k in d:
                    d[k] += 1
                else:
                    d[k] = 1
                if d[k] == len(split):
                    c += 1
    return c
        
        

print(everyYes(input("Day6/input.txt")))