# A. Calculating Function
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# For a positive integer n let's define a function f:

# f(n) =  - 1 + 2 - 3 + .. + ( - 1)n^xn

# Your task is to calculate f(n) for a given integer n.

# Input
# The single line contains the positive integer n (1 ≤ n ≤ 1015).

# Output
# Print f(n) in a single line.

# n = int(input())
# res = 0
# for i in range(1,n+1):
#     res += ((-1)**i)*i
# print(res)

n = int(input())
if n%2==0:
    print(n//2)
else:
    print(((n+1)//2)*-1)