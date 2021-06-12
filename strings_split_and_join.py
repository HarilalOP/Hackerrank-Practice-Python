#!/bin/python3

def solution_one(line):
    print(*line.split(), sep='-')

def solution_two(line):
    print("-".join(line.split()))

if __name__ == '__main__':
    s = input()
    solution_one(s)
    # solution_two(s)


    