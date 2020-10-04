# Given an integer n, count the number of groups of consecutive 1 bits in its binary representation.

# Example:

# For n = 1259, the output should be GroupedBits(n) = 4.
# The binary representation of 1259 is 10011101011, with the groups in bold.

# Input/Output:

# [execution time limit] 0.5 seconds

# [input] integer n
# 0 ≤ n ≤ 109.

# [output] integer

# The number of groups of 1 bits.

def groupedBits(n):
    if n==0:
        return 0
    a = bin(n)[2:].split('0')
    res = list(filter(lambda x : x!='',a))
    return len(res)

groupedBits(20)