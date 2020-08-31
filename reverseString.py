n = int(input())

for i in range(n):
    s = input()
    res = [i[::-1] for i in s.split()]
    print(' '.join(res))