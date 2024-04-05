#Given a list of numbers and a number k,
#return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def sum_from_list(numbers, k):
    for i in range(len(numbers)):
        for j in range(i +1 ,len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True 
        return False
    
numbers = [10,15,3,7]
k = 17 
print(sum_from_list(numbers,k))
