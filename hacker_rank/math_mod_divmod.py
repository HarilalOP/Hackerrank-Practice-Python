#!/bin/python3

def solution_one():
    a, b = int(input()), int(input())
    print(a//b, a%b, divmod(a, b), sep="\n")

def solution_two():
    a = divmod(int(input()), int(input()))
    print(*a, a, sep="\n")

if __name__ == '__main__':
    solution_one()
    # solution_two()
