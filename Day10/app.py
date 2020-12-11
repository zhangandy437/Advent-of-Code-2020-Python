def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return list(map(int, lines))

def p1(arr: [int]) -> int:
    ones = 0
    threes = 1
    arr.sort()
    last = 0
    for i in range(len(arr)):
        if arr[i] - last == 1:      ones += 1
        elif arr[i] - last == 3:    threes += 1
        last = arr[i]
    return ones * threes

def p2(arr: [int]) -> int:
    splits = 1
    falses = [1]
    arr.sort()
    count = 0
    last = 0
    
    def fillFalses(n):
        while len(falses) <= n:
            falses.append(falses[-1] * 2 + len(falses))
    
    def getSplits(n):
        if n < 3: return 2**n
        if n - 3 >= len(falses): fillFalses(n - 3)
        return 2**n - falses[n - 3]
    
    for i in range(len(arr) - 1):
        if arr[i + 1] - last < 4:
            count += 1
        else:
            splits *= getSplits(count)
            count = 0
        last = arr[i]
    splits *= getSplits(count)
    return splits
         
print(p2(input("Day10/input.txt")))

# Credit to u/kaur_virunurm on reddit
def p2copy(arr):
    from collections import Counter
    arr += [0]
    arr.sort()
    c = Counter({0:1})  
    for x in arr:  
        c[x+1] += c[x]  
        c[x+2] += c[x]  
        c[x+3] += c[x] 
    print(c[max(arr) + 3])
p2copy(input("Day10/input.txt"))

# Credit to u/Intro245 on reddit
def p2copy2(arr):
    a,*c=[0]*9
    n=1
    for b in sorted(map(int, arr)):
        c[b-a]+=1
        c+=[n,0,0][:b-a]
        a=b
        n=sum(c[-3:])
    print(c[1]*-~c[3],n)
p2copy2(input("Day10/input.txt"))