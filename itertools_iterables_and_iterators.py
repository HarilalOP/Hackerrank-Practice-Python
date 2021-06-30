#!/bin/python3

from itertools import combinations

def solution_one():
    n = int(input())
    indices = [idx + 1 for idx, char in enumerate(input().split()) if char == 'a']
    k = int(input())
    combs = [c for c in combinations(range(1, n+1), k)]
    print("{0:.3}".format(sum([any(t in c for t in indices) for c in combs])/len(combs)))

def solution_two():   
    _, a, k = input(),input().split(),int(input())
    combs = list(combinations(a, k))
    sub = [c for c in combs if 'a' in c]
    print("{0:.3}".format(len(sub)/len(combs)))

def solution_three():
    _, a, k = input(),input().split(),int(input())
    combs = list(combinations(a, k))
    sub = filter(lambda c: 'a' in c, combs)
    print("{0:.3}".format(len(sub)/len(combs)))

if __name__ == '__main__':
    s, r = input().split()
    solution_one()
    solution_two()
    solution_three()