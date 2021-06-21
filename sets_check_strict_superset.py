#!/bin/python3

if __name__ == '__main__':
    a = set(input().split())
    print(all([a.issuperset(set(input().split())) for _ in range(int(input()))]))
