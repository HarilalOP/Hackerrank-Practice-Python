#!/bin/python3

from collections import Counter

def solution_one(x, counter, n):
    total = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if counter[size]:
            total += price
            counter[size] -= 1
    print(total)

def solution_two(x, counter, n):
    total = []
    for _ in range(n):
        size, price = map(int, input().split())
        if size in counter and counter[size] > 0:
            total.append(price)
            counter.subtract(Counter([size]))
    print(total)

if __name__ == '__main__':
    x = int(input())
    counter = Counter(list(map(int, input().split())))
    n = int(input())
    solution_one()
    # solution_two()
