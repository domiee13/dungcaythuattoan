t = int(input())

for i in range(t):
    a = []
    n = int(input())
    a = [int(i) for i in input().split()]
    print(' '.join(sorted(a)))