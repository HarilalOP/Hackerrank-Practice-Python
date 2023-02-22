#!/bin/python3

if __name__ == '__main__':
    _, set_a = input(), set(map(int, input().split()))
    for _ in range(int(input())):
        operator = input().split()[0]
        set_b = set(map(int, input().split()))
        getattr(set_a, operator)(set_b)
        
    print(sum(set_a))