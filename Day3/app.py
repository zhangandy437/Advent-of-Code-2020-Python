def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def obstacle(slope, x_off, y_off):
    row_length = len(slope[0])
    x = 0
    y = 0
    total = 0
    while(y < len(slope)):
        if(slope[y][x] == "#"): total += 1
        x = (x + x_off) % row_length
        y += y_off
    return total

text = input("Day3/input.txt")

print(obstacle(text, 1, 1) * 
      obstacle(text, 3, 1) * 
      obstacle(text, 5, 1) * 
      obstacle(text, 7, 1) * 
      obstacle(text, 1, 2))
        
o = Test()
o.test()
o.test()
