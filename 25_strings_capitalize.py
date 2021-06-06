#!/bin/python3

import string

# Complete the solve function below.
def solution_one(s):
    print(" ".join((word.capitalize() for word in s.split(' '))))

def solution_two(s):
    print(string.capwords(s, ' '))

if __name__ == '__main__':
    s = input()
    solution_one(s)
    # solution_two(s)
