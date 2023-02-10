'''
   This file contains a fibonacci function that has a bug
'''
def fibonacci(n: int) -> int:
    '''Return the Fibonacci number F_n for positive
    values of n, where F_1 = 1, F_2 = 1,
    and F_n = Fn-1 + F_n-2, n > 2
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3) 2
    >>> fibonacci(7) 13
    '''
    a = 1
    b = 1
    for i in range (1, n): 
        a, b = b, a+b
    return a