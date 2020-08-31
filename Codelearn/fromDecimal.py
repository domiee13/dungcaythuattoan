# Chuyển đổi một số n thành một base cho trước.

# Ví dụ

# Với b = 2 và n = 13, đầu ra là fromDecimal(base, n) = "1101".
# Đầu vào/Đầu ra

# [giới hạn thời gian chạy] 0.5 seconds (cpp)

# [đầu vào] integer b

# Số nguyên dương.

# Điều kiện tiền đề:
# 2 ≤ b ≤ 9.

# [đầu vào] integer n

# Số nguyên dương.

# Điều kiện tiền đề:
# 10 ≤ n ≤ 109.

# [đầu ra] string

def fromDecimal(b,n):
    res = ""
    while n!=0:
        res = str(n%b)+res
        n//=b
    return res