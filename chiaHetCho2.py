# Cho số nguyên dương N.
# Nhiệm vụ của bạn là hãy xác định xem có bao nhiêu ước số của N chia hết cho 2?

# Input: Dòng đầu tiên là số lượng bộ test T (T ≤ 100).

# Mỗi bộ test gồm một số nguyên N (1 ≤ N ≤ 10^9)

# Output:  Với mỗi test, in ra đáp án tìm được trên một dòng. 

t = int(input())

for i in range(t):
    n= int(input())
    a = [i for i in range(1,n) if i%2==0 and n%i==0]
    print(len(a))