# Cho một mảng arr các số nguyên. Hãy tìm tổng trị tuyệt đối lớn nhất của các hoán vị của mảng đã cho bằng cách tìm tổng các trị tuyệt đối giữa hiệu các phần tử kề nhau ở trong một vòng tròn.

# Ví dụ:

# Với arr = [1, 2, 4, 8]. Đầu ra maxAbsSum(arr) = 18.
#      Giải thích:

#         - Nếu để mảng như ban đầu thì tổng các trị tuyệt đối là |1-2|+|2-4|+|4-8|+|8-1|=14

#         - Nếu hoán vị mảng thành [1,8,2,4] thì tổng các trị tuyệt đối là |1-8|+|8-2|+|2-4|+|4-1|=18.

from itertools import permutations
def sum(a):
    res = 0
    for i in range(len(a)-1):
        res+= abs(a[i]-a[i+1])
    return res+abs(a[len(a)-1]-a[0])
def maxAbsSum(arr):
    perm = list(permutations(arr))
    return max([sum(list(i)) for i in (perm)])