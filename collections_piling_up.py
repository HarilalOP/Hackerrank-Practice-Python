#!/bin/python3

from collections import deque

def solution_one():
    for _ in range(int(input())):
        _, d = input(), deque(map(int, input().split()))
        for e in reversed(sorted(d)):
            if d[0] == e:
                d.popleft()
            elif d[-1] == e:
                d.pop()
            else:
                print('No')
                break
        else:
            print('Yes')

def solution_two():
    # without collections
    for t in range(input()):
        _, lst = input(), map(int, input().split())
        l = len(lst)
        i = 0
        while i < l - 1 and lst[i] >= lst[i+1]:
            i += 1
        while i < l - 1 and lst[i] <= lst[i+1]:
            i += 1
        print("Yes") if i == l - 1 else print("No")

if __name__ == '__main__':
    solution_one()
    # solution_two()
