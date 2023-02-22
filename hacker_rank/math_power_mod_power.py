#!/bin/python3

if __name__ == '__main__':
    a, b, m = [int(input()) for _ in range(3)]
    print(*[pow(a, b), pow(a, b, m)], sep="\n")