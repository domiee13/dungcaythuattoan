# Một số nguyên tố được gọi là siêu nguyên tố nếu như ta lần lượt xóa các chữ số bên phải đi, ta vẫn được các số nguyên tố.

# Ví dụ 2333 là một số siêu nguyên tố vì khi ta lần lượt xóa các chữ số bên phải, thì ta được các số: [233, 23, 2] đều là các số nguyên tố.

# Idea: goi de quy isSuperPrime(n//10) khi n//10 con khac 0

def isSuperPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**1/2)+1):
        if n%i==0:
            return False
    return isSuperPrime(n//10) if n//10!=0 else True

