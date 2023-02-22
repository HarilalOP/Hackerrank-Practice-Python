#!bin/python3
from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(input())):
        item, price = input().rsplit(' ', 1)
        d[item] = d.get(item, 0) + int(price)
    for k, v in d.items():
        print(k, v)

