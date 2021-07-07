#!bin/python3
from collections import Counter, OrderedDict

def solution_one():
    c = Counter(sorted(input()))
    commons = c.most_common(3)
    print(*[" ".join(map(str, t)) for t in commons], sep="\n")

def solution_two():
    class OrderedCounter(Counter, OrderedDict):
        pass
    [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

if __name__ == '__main__':
    solution_one()
    # solution_two()

