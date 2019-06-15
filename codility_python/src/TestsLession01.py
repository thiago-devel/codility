


def printFibonacci(n):    
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c

def printTriangle(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' '),
        for j in range(2 * i - 1):
            print('*'),
        print

def printFactorialNumber(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(factorial)

printFactorialNumber(20)
printTriangle(10)
printFibonacci(100)