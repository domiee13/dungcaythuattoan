# Cho 1 tập hợp chứa số nguyên dương

# Hãy tính tổng các số từ 1 tới n mà chia hết cho 1 trong các số trong tập hợp trên.

# Ví dụ:

# Với arr=[1,2,3], n = 4, thì sumOfNumbers(arr,n) = 10
# Với arr=[11], n = 10, thì sumOfNumbers(arr,n) = 0

def sumOfNumbers(arr,n):
    return sum([i for i in range(1,n+1) if any([i%j==0 for j in arr])]) 