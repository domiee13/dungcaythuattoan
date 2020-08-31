# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

# Example

# For n = 6, l = 2, and r = 4, the output should be
# countSumOfTwoRepresentations(n, l, r) = 2.
# These ways are: 2 + 4 = 6 and 3 + 3 = 6.

def countSumOfTwoRepresentations(n, l, r):
    t = 0
    for a in range(l, r + 1):
        b = n - a
        if b < a: break
        if l <= a <= b <= r:
            t += 1
    return t
