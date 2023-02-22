
#!/bin/python3

import re

"""
count number of occurences of sub string in a given string
"""

def solution_one(string, sub_string):
    print(sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i+len(sub_string)] == sub_string]))

def solution_two(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:].startswith(sub_string):
            count += 1
    print(count)

def solution_three(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        string = string[string.find(sub_string) + 1:]
    print(count)

def solution_four(string, sub_string):
    count = 0
    i = string.find(sub_string)
    while i != -1:
        count += 1
        i = string.find(sub_string, i+1)
    print(count)

def solution_five(string, sub_string):
    print([string[i:i+len(sub_string)] for i in range(len(string))].count(sub_string))

def solution_six(string, sub_string):
    print(len(re.findall("(?=" + sub_string + ")", string)))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    solution_one(string, sub_string)
    # solution_two(string, sub_string)
    # solution_three(string, sub_string)
    # solution_four(string, sub_string)
    # solution_five(string, sub_string)
    # solution_six(string, sub_string)
