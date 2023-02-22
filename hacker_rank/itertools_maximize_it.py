#!/bin/python3

from itertools import product

if __name__ == '__main__':
    k, m = map(int,input().split())
    n = (list(map(int, input().split()))[1:] for _ in range(k))
    s = map(lambda x: sum(prod ** 2 for prod in x), product(*n))
    print(max(s))