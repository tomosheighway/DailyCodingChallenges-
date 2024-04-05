"""
Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

#TODO Currently will break if the array contains a 0 

def product_of_array(numbers):
    result = []
    total_product = 1
    
    for num in numbers:
        total_product *= num
    
    for num in numbers:
        result.append(total_product // num)
    
    return result


#Example 1
numbers = [1, 2, 3, 4, 5]
print(product_of_array(numbers)) 

#Example 2
numbers = [3, 2, 1]
print(product_of_array(numbers))  
