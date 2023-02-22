#!bin/python3
from collections import Counter, OrderedDict

def solution_one():
    d = OrderedDict()
    for _ in range(int(input())):
        item = input()
        d[item] = d.get(item, 0) + 1
    print(len(d))
    print(*d.values())

def solution_two():
    class OrderedCounter(Counter, OrderedDict):
        pass
    d = OrderedCounter(input() for _ in range(int(input())))
    print(len(d))
    print(*d.values())

def solution_three():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    counts = Counter(words)
    print(len(counts))
    print(*counts.values())

if __name__ == '__main__':
    solution_one()
    # solution_two()
    # solution_three()

