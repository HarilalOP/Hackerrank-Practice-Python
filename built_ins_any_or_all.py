#!/bin/python3

if __name__ == '__main__':
    n, l = int(input()), list(map(int, input().split()))
    print(all(e > 0 for e in l) and any(e == int(str(e)[::-1]) for e in l))

    