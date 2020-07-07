# Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm số xuất hiện nhiều hơn 1 lần trong dãy số và số thứ tự là nhỏ nhất.

# Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 10). Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu. Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 109).

# Output:  Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu không tìm được đáp án, in ra “NO”.
import sys
def solve(arr):
    for i in arr:
        if arr.count(i)>1:
            return i
    return "NO"

n = int(input())

for i in range(n):
    s = int(input())
    arr = []
    for i in range(s):
        arr.append(int(input()))
    print(solve(arr))

sys.exit(0)