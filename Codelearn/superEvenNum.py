# Hải vừa nghĩa ra một định nghĩa số siêu chẵn, theo Hải thì số n là số siêu chẵn khi:

# Bản thân n là số chẵn.
# Khi lần lượt xóa các chữ số bên phải của n thì nó vẫn là số chẵn.
# Ví dụ: 8248 là số siêu chẵn vì 8248, 824, 82, 8 là số chẵn.
# Hải có một số nguyên dương n, Hải muốn biết có bao nhiêu số siêu chẵn nhỏ hơn hoặc bằng n.

def isSuperEvenNum(n):
    if n%2!=0:
        return False
    return isSuperEvenNum(n//10) if n//10!=0 else True

def findSuperEvenNum(n):
    res= 0
    for i in range(1,n+1):
        if isSuperEvenNum(i):
            res+= 1
    return res