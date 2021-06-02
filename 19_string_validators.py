#!/bin/python3

def solution_one(s):
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

def solution_two(s):
    validators = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for val in validators:
        print(any(eval('c.{0}()'.format(val)) for c in s))

def solution_three(s):
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))

def solution_four(s):
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(c) for c in s))

if __name__ == '__main__':
    s = input()
    # solution_one(s)
    # solution_two(s)
    solution_three(s)