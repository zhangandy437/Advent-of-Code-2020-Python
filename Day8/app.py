def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def p1(instructions, accum = 0, counter = 0, sT = set()):
    running = True
    s = set()
    while running:
        if counter in s or counter in sT:
            return None
        s.add(counter)
        instruct = instructions[counter].split(" ")
        if instruct[0] == "jmp":
            counter += int(instruct[1])
        else:
            if instruct[0] == "acc":
                accum += int(instruct[1])
            counter += 1
        
        running = counter < len(instructions)
    return accum
    
def p2(instructions):
    accum = 0
    running = True
    counter = 0
    s = set()
    
    while running:
        if counter in s:
            return None
        s.add(counter)
        
        instruct = instructions[counter].split(" ")
        
        if instruct[0] == "jmp":
            hold = instructions[counter]
            instructions[counter] = "nop +0"
            test = p1(instructions, accum, counter + 1, s)
            if test:
                return test
            instructions[counter] = hold
            counter += int(instruct[1])
        else:
            if instruct[0] == "acc":
                accum += int(instruct[1])
            counter += 1
        
        running = counter < len(instructions)
    
    return accum


print(p2(input("Day8/input.txt")))