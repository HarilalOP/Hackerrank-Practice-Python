#!/bin/python3

if __name__ == '__main__':
    # input 4 lines: number of elements followed by elements space separated
    a, b = [set(map(int, input().split())) for _ in range(4)][1::2] 
    sd = a.symmetric_difference(b)
    print(*sorted(sd), sep="\n")
