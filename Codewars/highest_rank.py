# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.

# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
def highest_rank(arr):
    key = max([arr.count(i) for i in arr])
    res = []
    for i in arr:
        if arr.count(i)==key:
            res.append(i)
    return max(res)

#Another solution
def highest_rank1(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]