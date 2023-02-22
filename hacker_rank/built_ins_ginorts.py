#!/bin/python3

def solution_one():
    s = input()
    low, upp, odig, edig = ([] for _ in range(4))
    for l in s:
        if l.islower():
            low.append(l)
        elif l.isupper():
            upp.append(l)
        elif l.isdigit():
            if int(l) % 2 == 0:
                edig.append(l)
            else:
                odig.append(l)
    low.sort()
    upp.sort()
    odig.sort()
    edig.sort()
    print("".join(low + upp + odig + edig))

def getKey(x):
    if x.islower():
        return(1,x)
    elif x.isupper():
        return(2,x)
    elif x.isdigit() :
        if int(x)%2==1:
            return(3,x)
        else :
            return(4,x)

def solution_two():
    kv = lambda x: (
        int(x.isupper()) * 2 +
        int(x.isdigit()) * 3 +
        int(x.isdigit() and int(x) % 2 == 0), 
        x
    )
    print(*sorted(input(), key=kv), sep='')

def solution_three():
    print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x))), sep='')

if __name__ == '__main__':
    # solution_one()
    # solution_two()
    solution_three()
    