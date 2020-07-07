n = int(input())

a = []
b = []

for i in range(0,n):
    a.append(int(input()))

m  = int(input())
for i in range(0,m):
    b.append(int(input()))

c = sorted(a+b)

for i in c:
    print(i, end=" ")