#!/bin/python3

import string

def print_rangoli(size):
    l = string.ascii_lowercase
    m = 4 * size - 3
    arr = []
    for i in range(size):
        s = "-".join(l[i:size])
        arr.append((s[::-1]+s[1:]).center(m, "-"))
    print('\n'.join(arr[:0:-1] + arr)) 
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)