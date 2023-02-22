#!/bin/python3

if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    x, y, z, n = (int(input()) for _ in range(4))
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n])