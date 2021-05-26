#!/bin/python3

def solution_one(arr):
    print(sorted(list(set(arr)))[-2])

def solution_two(arr):
    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    solution_one(arr)
    # solution_two(arr)
    