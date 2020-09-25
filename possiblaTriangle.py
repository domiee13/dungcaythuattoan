# Count triangle create by a,b,c in range(n)

n = int(input())

count = 0
arr = [i for i in range(1,n+1)]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (arr[i]+arr[j]>arr[k] and arr[j]+arr[k]>arr[i] and arr[i]+arr[k]>arr[j]):
                count+=1
print(i)