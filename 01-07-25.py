"""
This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""

def fib(n): # iterative approach for returning nth fibonacci number 
    first, second = 0, 1
    for i in range(n):
        first, second = second, first + second

    return first
    
print(fib(10));     # n must be a +ve value. 
print(fib(50));
