"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import random

def rand5():
    return random.randint(1,5)              # random between 1 and 5 

def rand7():
    while True:
        num = (rand5() - 1) * 5 + rand5()   # rand number of 25    
        
        if num <= 21:                       # use modulo for even chance 
            return (num - 1) % 7 + 1

for i in range(7):                          # 7 test numbers 
    print(rand7())