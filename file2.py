print('hello suraj')

def multiply(first, second):
    return first * second

def fib_(n):
    first, second = 0, 1
    for _ in range(n):
        print(first)
        first, second = second, first + second


fib_(10)
