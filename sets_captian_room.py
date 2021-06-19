#!/bin/python3
def solution_one():
    k = int(input()) + 1
    room_nums = input().split()
    u = set() # unique room numbers
    a = set() # room numbers occured more than one
    for num in room_nums:
        if num in u:
            a.add(num)
        else:
            u.add(num)     
    c = u.difference(a)
    print(list(c)[0])

def solution_two():
    k,arr = int(input()),list()
    s = set(map(int, input().split()))
    print(((sum(s)*k)-(sum(arr)))//(k-1))

if __name__ == '__main__':
    solution_one()
    # solution_two()
