#!/bin/python3

def solution_one(s):
    for i in range(int(input())):
        line = input().split()
        if line[0]=="pop" :
            s.pop()
        elif line[0]=="remove" :
            s.remove(int(line[1]))
        elif line[0]=="discard" :
            s.discard(int(line[1]))
    print(sum(s))

def solution_two(s):
    for i in range(int(input())):
        c, *args = map(str,input().split())
        getattr(s,c) (*(int(x) for x in args))
    print(sum(s))

def solution_three(s):
    for _ in range(int(input())):
        eval('s.{0}({1})'.format(*input().split() + ['']))
    print(sum(s))

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    solution_one(s)
    solution_two(s)
    solution_three(s)

