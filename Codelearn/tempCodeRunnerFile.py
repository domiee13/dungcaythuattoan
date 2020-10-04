def groupedBits(n):
    if n==0:
        return 0
    a = bin(n)[2:].split('0')
    res = filter(lambda x : x!='',a)
    return len(res)

groupedBits(20)