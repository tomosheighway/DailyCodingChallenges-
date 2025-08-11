"""
Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a
palindrome. Do not convert the integer into a string.
"""

def palindrome_check(n):
    if n < 0:
        return False     #negative number cannot be palindrome 

    rev, temp = 0, n
    while temp:
        rev = rev * 10 + temp % 10    # add last digit from temp to rev 
        temp //= 10                   # now remove from temp 
    return n == rev

#Testing 
print(palindrome_check(121))  
print(palindrome_check(888))  
print(palindrome_check(678)) 
