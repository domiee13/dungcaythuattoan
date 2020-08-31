# Tìm chữ số cuối cùng của n! (giai thừa), khác 0.

# Ví dụ

# Với n = 5, đầu ra là LastDigitDiffZero (n) = 2.
# 5! = 1 · 2 · 3 · 4 · 5 = 120.
# Với n = 6, đầu ra là LastDigitDiffZero (n) = 2.
# 6! = 1 · 2 · 3 · 4 · 5 · 6 = 720.
# Với n = 10, đầu ra là LastDigitDiffZero (n) = 8.
# 10! = 3628800. 
# Đầu ra/Đầu vào

# [giới hạn thời gian chạy] 0,5 giây (c)
# [đầu vào]integer64 n
# Điều kiện tiền đề:
# 1 ≤ n ≤ 10 ^ 6.
# [đầu ra] integer
 

def lastDigitDiffZero(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    for i in str(res)[::-1]:
        if i!='0':
            return int(i)