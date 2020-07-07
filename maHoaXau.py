# Cho một sâu s chỉ gồm các ký tự viết thường, hãy viết hàm trả về chuỗi mã hóa của sâu này. Xem ví dụ để hiểu rõ hơn quá trình mã hóa.

# Ví dụ

# Test mẫu 1:

# Input	    Output
# aaabbaaac   a3b2a3c1
# Với s = "aaabbaaac" thì encodeString(s) = "a3b2a3c1".

s = input()
c = 0
res = ""
a = [i for i in s]
tmp = ""

while len(a)!=0:
    tmp = a[0]
    while len(a)>0 and tmp==a[0]:
        a.pop(0)
        c += 1    
    res += str(tmp)+str(c)
    c = 0

print(res)