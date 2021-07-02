#!bin/python3
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)
    
    for i in range(n):
        d[input()].append(i+1)
    
    for _ in range(m):
        item = input()
        if item in d:
            print(" ".join(map(str, d[item])))
        else:
            print(-1)

