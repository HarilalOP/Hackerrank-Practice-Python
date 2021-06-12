#!/bin/python3

def average(array):
    s = set(array)
    return round(sum(s) / len(s), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)