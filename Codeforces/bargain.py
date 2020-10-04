#Wrong answer
n = int(input())
a = [(i) for i in str(n)]

def gen(a):
    l = len(a)-1
    while a[l]==1:
        a[l] = 0
        l-=1
    if l>=0:
        a[l]=1

def check(a):
    for i in a:
        if i==0:
            return False
    return True

def sum(a):
    tmp = ""
    for i in a:
        if pos[a.index(i)]==1:
            tmp+=i
    return int(tmp) if len(tmp)>0 else 0
pos = [0 for i in range(len(a))]
res = 0
while not check(pos):
    res += sum(a)%((10**9)+7)
    gen(pos)
print(res%((10**9)+7))