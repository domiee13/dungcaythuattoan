import numpy

n,m = input().split(" ")
n =int(n)
m = int(m)
a = []
for i in range(n):
    tmp = []
    for c in input().split(" "):
        tmp.append(int(c))
    a.append(tmp)
    tmp = []
a = numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())