#!/bin/python3

if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = [set(map(int, input().split())) for _ in range(4)][1::2]
        print(a.issubset(b))
