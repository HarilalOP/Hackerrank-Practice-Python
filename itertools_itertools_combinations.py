#!/bin/python3

from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    s = sorted(s)
    combs = [''.join(c) for l in range(1, int(k) + 1) for c in combinations(s, l)]
    print(*combs, sep="\n")