# Given a number and a range, find the largest integer within the given range that's divisible by the given number.

# Example

# For left = 1, right = 10, and divisor = 3, the output should be
# maxDivisor(left, right, divisor) = 9.

# The largest integer divisible by 3 in range [1, 10] is 9.

def maxDivisor(left, right, divisor):
    res = [i for i in range(left,right+1) if i%divisor==0]
    if len(res)==0:
        return -1
    return max([i for i in range(left,right+1) if i%divisor==0]) 
