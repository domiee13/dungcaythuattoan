# Cho một dãy số n có a chữ số, hãy xóa b chữ số bất kỳ ra khỏi n sao cho kết quả là số nhỏ nhất có thể theo thứ tự ban đầu.

# Nếu không thể, hãy trả về 'empty'.

# Ví dụ:

# Với n = '8792180', a = 7 và b = 2 thì min_number(n, a, b) = '72180'
# Với n = '912001', a = 6 và b = 3 thì min_number(n, a, b) = '1'
# [Đầu vào/Đầu ra]:

# [Thời gian chạy]: 0.5s với C++, 3s với Java và C#, 4s với Python, Go và JavaScript.
# [Đầu vào]: String n - Integers a, b
# 1 <= a <= 10^3
# 1 <= b <= 10^3
# [Đầu ra]: String

# empty khi a==b
def min_number(n,a,b):
    if a==b:
        return "empty"
    arr = [int(i) for i in str(n)]
    for i in range(b):
        arr.remove(max(arr))
    res = [str(i) for i in arr]
    return str(int(''.join(res))) 