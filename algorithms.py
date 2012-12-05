from random import *

def insertionSort(li):
    for i in range(1, len(li)):
        value = li[i]
        x = i - 1
        while x >= 0:
            if value < li[x]:
               li[x+1] = li[x]
               li[x] = value
               x -= 1
            else:
                break
    return li

def binarySearch(li, v):
    # Takes a sorted list (li) and searches for a value (v)
    lo= 0; hi = len(li)-1
    while True:
        if hi < lo:
            return -1
        mid = (lo + hi) // 2
        if li[mid] < v:
            lo = mid + 1
        elif li[mid] > v:
            hi = mid -1
        else:
            return mid

def randListComp(l, n):
    return [randint(0,n) for l in range(l)]

def main():
    print(binarySearch(insertionSort(randListComp(14,14)), randint(0,14)))

main()


