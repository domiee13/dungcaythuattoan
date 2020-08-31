# You are given a positive integer x and you should perform n operations, where on the ith operation you increase x in such a way that its new value is divisible by i (operations are numbered from 1 to n).

# Find the minimal value of x you can obtain by performing n operations described above.

# Example

# For x = 9 and n = 5, the output should be
# increasingNumber(x, n) = 15.

def increasingNumber(x, n):
    for i in range(1,n+1):
        while x % i:
            x += 1
    return x
