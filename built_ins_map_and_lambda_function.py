#!/bin/python3

cube = lambda x: x ** 3 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# second solution
def fibonacci(n):
    fib = [0, 1]
    for i in range(2,n):
        fib.append(fib[i-2] + fib[i-1])
    return(fib[0:n])

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))