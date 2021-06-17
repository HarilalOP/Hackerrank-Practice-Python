#!/bin/python3

if __name__ == '__main__':
    # first and third line contain number of elements
    # second and fourth line contain elements in set
    e, f = [set(input().split()) for _ in range(4)][1::2]
    print(len(e.difference(f)))

    # Solution 2
    _,a,_,b=eval("set(input().split()),"*4)
    print(len(a-b))