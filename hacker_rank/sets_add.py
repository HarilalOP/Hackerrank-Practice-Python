#!/bin/python3

def solution_one():
    n = input()
    s = set()
    for i in range(int(n)):
        s.add(input())
    print(len(s))

def solution_three():
    n = int(input())
    s = set([input() for _ in range(n)])
    print(len(s))

def solution_two():
    print(len({input() for _ in range(int(input()))}))

if __name__ == '__main__':
    solution_one()
    solution_two()