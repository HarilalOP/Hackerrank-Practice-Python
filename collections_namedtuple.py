#!bin/python3
from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    Student = namedtuple('Student', input())
    total = sum([int(Student(*input().split()).MARKS) for _ in range(n)])
    print('{:.2f}'.format(total/n))

