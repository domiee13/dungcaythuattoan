# CoderToDev Đơn giản 100 Điểm
# Giới hạn ký tự: 3000
# Cho số nguyên n, k và một dãy số nguyên a. Bạn hãy tìm cách chia dãy đã cho thành hai phần, trong đó một phần có k phần tử và một phần có n - k phần tử sao cho độ lệch giữa hai phần là lớn nhất. Độ lệch giữa hai phần được tính bằng cách lấy tổng của phần này trừ cho tổng phần kia. Hãy trả về độ lệch lớn nhất đó

# Ví dụ:

# Với n = 5, k = 2, a = [8,4,5,2,10] thì kết quả maxDiff(n, k, a) = 17

# Giải thích: Ta có thể chia thành hai phần như sau
# [2,4] và [5,8,10] -> Độ lệch là 17 -> Lớn nhất

def max_diff(n,k,a):
    a = sorted(a)
    return sum(a[max(k,n-k):])-sum(a[:max(k,n-k)])