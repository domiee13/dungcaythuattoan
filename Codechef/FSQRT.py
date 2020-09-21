# Input
# The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

# Output
# For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.

# Constraints
# 1<=T<=20
# 1<=N<=10000
# Input:
# 3
# 10
# 5
# 10000

# Output:
# 3
# 2
# 100

t = int(input())

for i in range(t):
    print(int(int(input())**0.5))