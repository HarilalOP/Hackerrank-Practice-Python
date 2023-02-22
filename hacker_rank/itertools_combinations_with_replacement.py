#!/bin/python3

from itertools import combinations_with_replacement as cwr

if __name__ == '__main__':
    s, k = input().split()
    s = sorted(s)
    print(*[''.join(c) for c in cwr(s, int(k))], sep="\n")