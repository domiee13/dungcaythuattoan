# Một số được xem là số "giàu có" khi tổng các ước nguyên dương chính thức của nó (không tính chính nó) lớn hơn số đó. Cho biết n, hãy kiểm tra xem liệu đó có là một số "giàu có" hay không. Nếu nó là số "giàu có" thì trả về true, nếu không trả về false.

# Ví dụ:

# Với n = 12 thì richNumber(n) = true vì 1 + 2 + 3 + 4 + 6 = 16 > 12
# Với n = 4 thì richNumber(n) = false vì 1 + 2 = 3 < 4

def richNumber(n):
    if n<0:
        return False
    a = [i for i in range(1,n) if n%i==0]
    if sum(a)>n:
        return True
    return False