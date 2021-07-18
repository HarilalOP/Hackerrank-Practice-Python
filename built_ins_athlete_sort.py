#!/bin/python3

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    k = int(input())
    for sub_list in sorted(arr, key = lambda x: x[k]):
        print(*sub_list)

    