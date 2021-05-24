#!/bin/python3

def solution_one(n):
    for i in range(1,n+1):
        print(i, end='')

def solution_two(n):
    print(*[i for i in range(1, n+1)], sep='')

def solution_three(n):
    print(*range(1, n+1), sep='')

def solution_four(n):
    [print(i+1,end="") for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    solution_one(n)
    # solution_two(n)
    # solution_three(n)
    # solution_four(n)
    