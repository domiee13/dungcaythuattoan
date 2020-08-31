# Find the smallest integer that is divisible by all integers on a given interval [left, right].

# Example

# For left = 2 and right = 4, the output should be
# smallestMultiple(left, right) = 12.

from fractions import gcd
def smallestMultiple(left, right):
    res = left
    for i in range(left,right+1):
        res = (res*i)//gcd(res,i)
    return res
