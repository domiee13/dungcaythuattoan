# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input().split(" ")
m = int(input())
b = input().split(" ")
c = set(a+b)
res = []
for i in c:
    if not(i in a and i in b):
        res.append(int(i))
res = sorted(res)
for i in res:
    print(i)