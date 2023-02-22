#!/bin/python3

import math

if __name__ == '__main__':
    ab, bc = int(input()),int(input())
    ac=math.hypot(ab,bc) 
    res=round(math.degrees(math.acos(bc/ac)))
    print(res, chr(176), sep='')
