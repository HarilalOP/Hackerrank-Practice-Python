#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    marksheet = [[input(), float(input())] for _ in range(n)]
    second_heighest = sorted(list(set([mark for _, mark in marksheet])))[1]
    print("\n".join([name for name, mark in sorted(marksheet) if mark == second_heighest]))