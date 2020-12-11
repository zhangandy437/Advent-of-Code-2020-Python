def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return list(map(lambda x: int(x), lines))

def p1(arr, off: int) -> int:
    pastOff = set()
    
    def inSet(s: set, arr: [int], left: int, right: int, target: int) -> bool:
        for i in range(left, right):
            if target - arr[i] in s:
                return True
        return False
    
    for i in range(len(arr)):
        if i < off:
            pastOff.add(arr[i])
        else:
            if not inSet(pastOff, arr, i - off, i, arr[i]):
                return arr[i]
            pastOff.remove(arr[i - off])
            pastOff.add(arr[i])
    return -1
    
def p2(arr, target):
    left = 0
    right = 0
    curSum = arr[0]
    while curSum != target:
        if curSum < target:
            right += 1
            curSum += arr[right]
        if curSum > target:
            curSum -= arr[left]
            left += 1
    
    small = target
    big = 0
    for i in range(left, right + 1):
        if small > arr[i]:
            small = arr[i]
        if big < arr[i]:
            big = arr[i]
    return small + big

# print(p2(input("Day9/input.txt"), 85848519))
import collections
test = collections.deque()

print()