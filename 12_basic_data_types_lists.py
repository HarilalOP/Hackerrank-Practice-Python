#!/bin/python3

def solution_one(n):
    arr = []
    for _ in range(n):
        line = input().split()
        command = line[0]
        args = line[1:]
        if command !="print":
            command += "("+ ",".join(args) +")"
            eval("arr."+command)
        else:
            print(arr)

def solution_two(n):
    arr = []
    for _ in range(n):
        line = input().split()
        command = line[0]
        args = line[1:]
        if command !="print":
            eval('arr.{0}{1}'.format(command,tuple(map(int,args))))
        else:
            print(arr)

if __name__ == '__main__':
    n = int(input())
    solution_one(n)
    # solution_two(n)

    