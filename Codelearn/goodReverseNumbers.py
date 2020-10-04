def sum(n):
    if str(n)[::-1][0]=='0':
        return 0
    return n + int(str(n)[::-1])
def check(n):
    a = [1,3,5,7,9]
    for i in str(n):
        if int(i) not in a:
            return False
    return True
def goodReverseNumbers(n):
    count  = 0
    for i in range(11,n):
        if check(sum(i)):
            count +=1
            print(i,end = ":")
            print(sum(i))
    return count
n = int(input())
print(goodReverseNumbers(n))