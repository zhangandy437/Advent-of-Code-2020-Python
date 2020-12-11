# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# TEST NUM OCCUPIED = 37
deltas = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
import copy

def p1(path: str, tolerance = 4) -> int:
    seats = [[y for y in x.strip()] for x in open(path)]
    total = 0
    print(len(seats), len(seats[0]))
    def findL(arr, x, y):
        nx = x
        ny = y
        num = 0
        for i in deltas:
            nx += i[0]
            ny += i[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == "L":
                num += 1
            nx = x
            ny = y
        return num
    
    def printSeats(seats):
        for i in seats:
            hold = ""
            for j in i:
                hold += j
            print(hold)
    
    def markO(arr, x, y):
        nx = x
        ny = y
        for i in deltas:
            nx += i[0]
            ny += i[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == "L":
                arr[nx][ny] = "O"
            nx = x
            ny = y
    
    current = 1
    while current:
        current = 0
        prev = copy.deepcopy(seats)
        occ = []
        # Find for sures
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and findL(prev, i, j) < tolerance:
                    current += 1
                    seats[i][j] = "#"
                    total += 1
                    occ.append([i, j])
        for i in occ:
            markO(seats, i[0], i[1])
    
    return total
# p1("Day11/test.txt")
def p2(path: str, tolerance = 5) -> int:
    seats = [[y for y in x.strip()] for x in open(path)]
    total = 0
    print(len(seats), len(seats[0]))
    def findL(arr, x, y):
        nx = x
        ny = y
        num = 0
        for i in deltas:
            nx += i[0]
            ny += i[1]
            while 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == ".":
                nx += i[0]
                ny += i[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == "L":
                num += 1
            nx = x
            ny = y
        return num
    
    def printSeats(seats):
        for i in seats:
            hold = ""
            for j in i:
                hold += j
            print(hold)
    
    def markO(arr, x, y):
        nx = x
        ny = y
        for i in deltas:
            nx += i[0]
            ny += i[1]
            while 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == ".":
                nx += i[0]
                ny += i[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == "L":
                arr[nx][ny] = "O"
            nx = x
            ny = y
    
    current = 1
    while current:
        current = 0
        prev = copy.deepcopy(seats)
        occ = []
        # Find for sures
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == "L" and findL(prev, i, j) < tolerance:
                    current += 1
                    seats[i][j] = "#"
                    total += 1
                    occ.append([i, j])
        for i in occ:
            markO(seats, i[0], i[1])
    
    return total

def countSeatsOccupied(seats):
    c = 0
    for i in "".join(seats): c += 1 if i == "#" else 0
    return c
# print(countSeatsOccupied([x.strip() for x in open("Day11/testans.txt")]))

print(p2("Day11/input.txt"))