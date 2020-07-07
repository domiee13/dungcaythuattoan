# Cho dãy số A[] có N phần tử. Nhiệm vụ của bạn là xác định xem tồn tại tập con của A sao cho tổng các phần tử của chúng bằng số K cho trước hay không?

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

# Mỗi test bắt đầu bởi 2 số nguyên N và K (1 ≤ N ≤ 100, 0 ≤ K ≤ 10000).

# Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 100).

# Output: 

# Với mỗi test, in ra “YES” nếu tồn tại tập con thỏa mãn, in ra “NO” trong trường hợp ngược lại.

t = int(raw_input())

for i in range(t):
    n, k = raw_input().split(" ")
    n = int(n)
    k = int(k)
    a = []
    ok = False
    for i in range(n):
        a.append(int(input()))
    for i in a:
        if (k-i) in a:
            print("YES")
            ok = True
            break
    if not ok:
        print("NO")