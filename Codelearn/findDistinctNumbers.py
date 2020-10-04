# Given an array a, your task is to find the distinct numbers in it and return them in the order that they appear in a. The input array might contain duplicate numbers, while the resulting array should contain only one instance of each number.

# Example:

# For a = [8, 4, 8, 4, 20], the output should be findDistinctNumbers(a) = [8, 4, 20].
# Input/Output:

# [execution time limit] 0.5 seconds 

# [input] array.integer a

# An array of integers. 0 ≤ a.length ≤ 8000, and -109 ≤ a[i] ≤ 109.

# [output] array.integer

# An array containing the distinct integers of the given array in the order in which they appear.

def findDistinctNumbers(a):
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    return res
#another solution
def findDistinctNumbers1(a):
    return list(dict.fromkeys(a))