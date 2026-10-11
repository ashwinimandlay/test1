print('hello world')

def multiply(a, b):
    return a * b

def fib_(n):
    first, second = 0, 1
    for _ in range(n):
        print(first)
        first, second = second, first + second


fib_(10)
