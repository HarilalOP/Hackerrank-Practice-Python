#!/bin/python3

def solution_one(a, b):
    print(a + b, a - b, a * b, sep='\n')

def solution_two(a, b):
    print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    solution_one(a, b)
    # solution_two(a, b)