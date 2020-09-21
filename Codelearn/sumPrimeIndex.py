# D.A.N_3002 Đơn giản 100 Điểm
# Giới hạn ký tự: 3000
# Cho mảng arr chứa các số nguyên. Bạn hãy tính tổng các phần tử ở các vị trí là số nguyên tố trong mảng arr. Biết các vị trí trong mảng đếm bắt đầu từ 1.

# Ví dụ:

# Với arr = [1, 2, 3, 4, 5, 6, 7] thì sumPrimeIndex(arr) = 17.
# Giải thích: các vị trí 2, 3, 5 7 là các vị trí số nguyên tố. ta có arr[2]+arr[3]+arr[5]+arr[7]= 2+3+5+7 = 17

def isPrime(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
def sumPrimeIndex(arr):
    return sum([arr[i] for i in range(len(arr)) if isPrime(i)])
print(sumPrimeIndex([1,2,3,2, 1, 4, 1, 4]))
print(isPrime(3))