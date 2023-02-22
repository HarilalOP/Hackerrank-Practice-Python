#!/bin/python3

import re

if __name__ == '__main__':
    regex = '^[+-]?[0-9]*\.[0-9]+$'
    for _ in range(int(input())):
        print(bool(re.match(regex, input())))

    