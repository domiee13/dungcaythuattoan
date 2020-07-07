# Số siêu nguyên tố là số:

# Bản thân nó là số nguyên tố.
# Khi xóa đi lần lượt các chữ số sau cùng của nó, thì số mới vẫn là số nguyên tố.
# Ví dụ 2393 là số siêu nguyên tố vì 2393, 239, 23, 2 là số nguyên tố.

# Cho một số n, hãy đưa số dãy số siêu nguyên tố nhỏ hơn hoặc bằng n, các số đã được sắp xếp tăng dần.

# Ví dụ:

# Test mẫu 1:

# Input	    Output
# 30          2 3 5 7 23 29 


# Với n = 30 thì superPrimeNumber(n) = [2, 3, 5, 7, 23, 29];
# Vì các số 2, 3, 5, 7, 23 và 29 đều là số siêu nguyên tố và nhỏ hơn hoặc bằng 30.
def isPrime(n):
    n = int(n)
    if(n<2):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def isSuperPrime(n):
    num = ""
    arr = [i for i in str(n)]
    if not isPrime(n):
        return False
    while len(arr)>0:
        arr.pop(len(arr)-1)
        if len(arr)>0:  
            for i in arr:
                num+=i
            if not isPrime(int(num)):
                return False
            num = ""
    return True

n = int(input())

res = [i for i in range(0,n) if isSuperPrime(i)]

for i in res:
    print(i, end=" ")