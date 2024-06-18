"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28."""


def sum_digits(num):            #function to sum numbers 
    return sum(int(digit) for digit in str(num))

def nth_PN(n):                  # function for nth perfect number 
    count = 0
    num = 19                    # start with 19 as smallest PN
    
    while True:
        if sum_digits(num) == 10:
            count += 1
            if count == n:
                return num
        num += 1

# Tests
print(nth_PN(1))  #19
print(nth_PN(2))  #28
print(nth_PN(3))  # 37
