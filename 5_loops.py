#!/bin/python3

def solution_one(n):
    for i in range(n):
        print(i ** 2)

def solution_two(n):
    [print(i ** 2) for i in range(n)]

def solution_three(n):
    print(*[i**2 for i in range(n)], sep='\n')

if __name__ == '__main__':
    n = int(input())
    solution_one(n)
    # solution_two(n)
    # solution_three(n)
