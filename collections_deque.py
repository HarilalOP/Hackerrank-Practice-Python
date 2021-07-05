#!/bin/python3

from collections import deque

def solution_one():
    d = deque()
    for _ in range(int(input())):
        command, *args = input().split();
        getattr(d, command)(*(int(x)for x in args))
    print(" ".join(map(str, d)))

def solution_two():
    d = deque()
    for _ in range(int(input())):
        inp = input().split()
        getattr(d, inp[0])(*inp[1:])
    print(*d)

def solution_three():
    d = deque()
    for _ in range(int(input())):
        command, *args = input().split()
        getattr(d, command)(*args)
    print(*d)

if __name__ == '__main__':
    solution_one()
    # solution_two()
    # solution_three()
