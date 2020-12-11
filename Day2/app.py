def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def numValid(arr) -> int:
    total = 0
    for i in arr:
        cur = i.split(" ")
        bounds = cur[0].split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        letter = cur[1][0]
        letters_in_word = 0
        for l in cur[2]:
            if l == letter: letters_in_word += 1
        if letters_in_word >= lower and letters_in_word <= upper: total += 1
    return total

def partTwo(arr) -> int:
    total = 0
    for i in arr:
        cur = i.split(" ")
        bounds = cur[0].split('-')
        lower = int(bounds[0])
        upper = int(bounds[1])
        letter = cur[1][0]
        letters_in_word = 0
        if cur[2][lower - 1] == letter: letters_in_word += 1
        if cur[2][upper - 1] == letter: letters_in_word += 1
        if letters_in_word == 1: total += 1
    return total

print(partTwo(input("Day2/input.txt")))