#!/usr/bin/python3


def sort(arr):
    n = len(arr)-1
    for x in range(n):
        for y in range(n):
            if(arr[y] > arr[y+1]):
                arr[y], arr[y+1] = arr[y+1], arr[y] 
    return arr

print(sort([100,2,31,34,1,12,0,0,0]))
