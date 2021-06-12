#!/bin/python3

def solution_one(s):
    print(s.swapcase())

def solution_two(s):
    s = "".join([l.lower() if l.isupper() else l.upper() for l in s])
    print(s)

if __name__ == '__main__':
    s = input()
    solution_one(s)
    # solution_two(s)


    