import re

def input(path):
    f = open(path, "r")
    lines = f.read().split("\n\n")
    f.close()
    return lines

def p1(arr):
    valid = 0
    fields = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    for i in arr:
        cur = 0
        string = re.split("\n| ", i)
        for j in string:
            if j[0:3] in fields: cur += 1
        if cur == len(fields): valid += 1
    return valid

def byrV(s):
    return yearV(s, 1920, 2002)

def iyrV(s):
    return yearV(s, 2010, 2020)

def eyrV(s):
    return yearV(s, 2020, 2030)

def yearV(s, lower, upper):
    year = int(s)
    return len(s) == 4 and year >= lower and year <= upper

def hgtV(s):
    length = len(s)
    metric = s[length - 2:length]
    num = 0
    try:
        num = int(s[0: length - 2])
    except ValueError:
        return False
        
    if metric == "cm":
        return num >= 150 and num <= 193
    else:
        return num >= 59 and num <= 76
    
def hclV(s):
    return len(s) == 7 and s[0] == '#' and re.compile('([a-f]|[0-9]){6,}').match(s[1:len(s)])

def eclV(s):
    return s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def pidV(s):
    return len(s) == 9 and re.compile('([0-9]){9,}').match(s)

def p2(arr):
    valid = 0
    fields = {"ecl": eclV, "pid": pidV, "eyr": eyrV, "hcl": hclV, "byr": byrV, "iyr": iyrV, "hgt": hgtV}
    for i in arr:
        cur = 0
        string = re.split("\n| ", i)
        for j in string:
            if j[0:3] in fields and fields[j[0:3]](j[4:len(j)]): cur += 1
        if cur == len(fields): valid += 1
    return valid

# print(p1(input("Day4/input.txt")))
print(p2(input("Day4/input.txt")))