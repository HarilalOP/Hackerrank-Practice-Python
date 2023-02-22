#!/bin/python3

if __name__ == '__main__':
    n, x = map(int, input().split())
    sub_scores = [list(map(float, input().split())) for _ in range(x)]
    print(*[round(sum(t)/len(t), 1) for t in zip(*sub_scores)], sep="\n")

    