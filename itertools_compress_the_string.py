#!/bin/python3

from itertools import groupby

if __name__ == '__main__':
    print(*[(len(list(v)), int(k)) for k, v in groupby(input())])