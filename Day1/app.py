def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return list(map(lambda x: int(x), lines))

def twoSum(arr, target, left, right):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while(left < right and arr[left] + arr[right] != target):
        if(arr[left] + arr[right] > target): right -= 1
        else: left += 1
    return [arr[left], arr[right]]

def twoSumDict(arr, target, left, right):
    d = set()
    for i in arr:
        diff = target - i
        if(diff in d): return [diff, i]
        else: d.add(i)
    return None

def threeSum(arr, target):
    arr.sort()
    for i in range(0, len(arr) - 1):
        two = twoSumDict(arr, target - arr[i], i + 1, len(arr) - 1)
        if(two != None): return [arr[i], two[0], two[1]]
    return None

import math
sums = threeSum(input('Day1/input.txt'), 2020)
print(sum(sums))
print(math.prod(sums))