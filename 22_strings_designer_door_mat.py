#!/bin/python3
def solution_one(n, m):
    for i in range(1, n, 2): 
        print((i * '.|.').center(m, '-'))
    print(("WELCOME").center(m, '-'))
    for i in range(n-2, -1, -2): 
        print((i * '.|.').center(m, '-'))

def solution_two(n, m):
    pattern = [(i * '.|.').center(m, '-') for i in range(1, n, 2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    # solution_one(n, m)
    solution_two(n, m)