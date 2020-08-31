# Given two sorted arrays of integers, check if there is at least one element which occurs in both arrays.

# Example

# For arr1 = [1, 2, 3, 5] and arr2 = [1, 4, 5], the output should be
# checkSameElementExistence(arr1, arr2) = true;
# For arr1 = [1, 3, 5] and arr2 = [-2, 0, 2, 4, 6], the output should be
# checkSameElementExistence(arr1, arr2) = false.

def checkSameElementExistence(arr1, arr2):
    s = list(set(arr1+arr2))
    for i in s:
        if i in arr1 and i in arr2:
            return True
    return False
