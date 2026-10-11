print('hello world')

def fib_(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


fib_(10)
