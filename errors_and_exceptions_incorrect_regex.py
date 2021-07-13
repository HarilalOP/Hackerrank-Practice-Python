#!bin/python3

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        is_valid = True
        try:
            re.compile(input())
        except re.error:
            is_valid = False
        print(is_valid)