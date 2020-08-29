# Một số gọi là số đẹp nếu tất cả các chữ số trong số đó đều giống nhau. ví dụ 111, 22, 3 là các số đẹp.

# Cho số nguyên dương a và b, Hãy đưa ra số lượng các số đẹp không nhỏ hơn a và không vượt quá b.

# Ví dụ:

# Với a = 8 và b = 12 thì countNumbersBeautiful(a, b) = 3.
# Giải thích: 3 số đẹp đó là 8, 9, 11.

# Với a = 11 và b = 20 thì countNumbersBeautiful(a, b) = 1.

def isBeautifulNum(n):
    return len(set([i for i in str(n)]))==1

def countNumbersBeautiful(a,b):
    res = 0
    for i in range(a,b+1):
        if isBeautifulNum(i):
            res+=1
    return res 

print(countNumbersBeautiful(8,12))