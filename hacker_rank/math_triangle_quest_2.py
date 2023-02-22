#!/bin/python3

def solution_one():
    for i in range(1,int(input())+1):
        print(((10**i-1)//9)**2) 

def solution_two():
    for i in range(1,int(input())+1):
        print(*[j for j in range(1, i + 1)] + [j for j in range(i - 1, 0, -1)], sep='')

if __name__ == '__main__':
    solution_one()
    # solution_two()
