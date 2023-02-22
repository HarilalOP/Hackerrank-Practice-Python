#!/bin/python3

def solution_one():
    print(int(input()) ** int(input()) + int(input()) ** int(input()))

def solution_two():
    a, b, c, d = (int(input) for _ in range(4))
    print(pow(a, b) + pow(c, d))

if __name__ == '__main__':
    solution_one()
    # solution_two()
