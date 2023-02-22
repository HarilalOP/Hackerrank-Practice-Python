#!/bin/python3

def solution_one():
    n, m = map(int, input().split())
    arr = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    h = 0
    for e in arr:
        if e in a:
            h += 1
        elif e in b:
            h -= 1
    print(h)

def solution_two():
    n, m = map(int, input().split())
    arr = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    print(sum([(i in a) - (i in b) for i in arr]))

if __name__ == '__main__':
    solution_one()
    # solution_two()
