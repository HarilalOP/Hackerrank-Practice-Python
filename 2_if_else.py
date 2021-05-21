#!/bin/python3

import math
import os
import random
import re
import sys

def solution_one(n):
    if n % 2 != 0:
        print('Weird')
    elif n in range(2, 6):
        print('Not Weird')
    elif n in range(6, 21):
        print('Weird')
    elif n > 20:
        print('Not Weird')

def solution_two(n):
    check = {True: "Not Weird", False: "Weird"}
    print(check[n%2==0 and (n in range(2,6) or n > 20)])

if __name__ == '__main__':
    n = int(input().strip())
    solution_one(n)
    # solution_two(n)