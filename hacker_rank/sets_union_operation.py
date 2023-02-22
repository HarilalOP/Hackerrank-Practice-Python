#!/bin/python3

if __name__ == '__main__':
    # first and third line contain number of elements
    # second and fourth line contain elements in set
    e, f = [set(input().split()) for _ in range(4)][1::2]
    print(len(e.union(f)))