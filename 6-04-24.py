"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def first_missing_positive(numbers):
    n = len(numbers)

    for i in range(n):
        if numbers[i] <= 0 or numbers[i] > n:
            numbers[i] = 0

    for i in range(n):
        if numbers[i] != 0:
            index = abs(numbers[i]) - 1
            if numbers[index] > 0:
                numbers[index] *= -1

    for i in range(n):
        if numbers[i] >= 0:
            return i + 1

    return n + 1

print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))


# --------------------A second more simple approach using sets.--------------------------------
# This solution is simpler but does require more space in comparison with the first soltuion but does have a lower n value. 

def first_missing_positive2(numbers):
    numbers_set = set(numbers)
    missing = 1

    while missing in numbers_set:
        missing += 1

    return missing

print(first_missing_positive2([3, 4, -1, 1]))
print(first_missing_positive2([1, 2, 0]))

