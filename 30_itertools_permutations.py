#!/bin/python3

from itertools import permutations

def solution_one(s, r):
    print("\n".join(["".join(t) for t in permutations(sorted(s), int(r))]))

def solution_two(s, r):   
    print(*["".join(t) for t in permutations(sorted(s), int(r))], sep="\n")

if __name__ == '__main__':
    s, r = input().split()
    solution_one(s, r)
    # solution_two(s, r)