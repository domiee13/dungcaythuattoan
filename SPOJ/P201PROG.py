import math

a = (1+math.sqrt(5))/2
b = (1-math.sqrt(5))/2

n = int(input())

res = (1/math.sqrt(5)) * (a**n-b**n)
print(math.ceil(res))