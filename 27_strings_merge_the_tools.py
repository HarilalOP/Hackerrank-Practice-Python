#!/bin/python3

def solution_one(string, k):
    while string:
        unique = ''
        for c in string[:k]:
            if c not in unique:
                unique += c
        print(unique)
        string = string[k:]

def solution_two(string, k):
    for i in range(0, len(string), k):
        unique = ''
        for c in string[i: i+k]:
            if c not in unique:
                unique += c
        print(unique)

def solution_three(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d ]))
            
if __name__ == '__main__':
    string, k = input(), int(input())
    solution_one(string, k)
    # solution_two(string, k)
    # solution_three(string, k)