#!bin/python3
from datetime import datetime
from dateutil import parser

def solution_one(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, fmt)
    t2 = datetime.strptime(t2, fmt)
    diff = int(abs((t1 - t2).total_seconds()))
    return diff

def solution_two(t1, t2):
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)
    diff = int(abs((t1 - t2).total_seconds()))
    return diff

if __name__ == '__main__':
    for t_itr in range(int(input())):
        t1 = input()
        t2 = input()
        delta = solution_one(t1, t2)
        # delta = solution_two(t1, t2)
        print(delta)