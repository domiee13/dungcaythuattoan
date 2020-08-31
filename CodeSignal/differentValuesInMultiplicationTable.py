# Define a multiplication table of size n by m as follows: such table consists of n rows and m columns. Cell on the intersection of the ith row and the jth column (i, j > 0) contains the value of i * j.

# Given integers n and m, find the number of different values that are found in the table.

# Example

# For n = 3 and m = 2, the output should be
# differentValuesInMultiplicationTable(n, m) = 5.

def differentValuesInMultiplicationTable(n, m):
    res = []
    a =[[x*y for x in range(1,n+1) for y in range(1,m+1)]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            res.append(a[i][j])
    return len(set(res))
