# DAN đang viết một chương trình xử lý chuỗi như sau: Cho vào chuỗi s1 và s2, hãy xóa tất cả các ký tự của chuỗi s1 mà ký tự đó xuất hiện ở s2. Hãy giúp DAN viết chương trình đó.

# Ví dụ:

# Với s1 = "abcdd" và s2 = "ad" thì removeChar(s1, s2) = "bc".
# Với s1 = "bbbccddd" và s2 = "av" thì removeChar(s1, s2) = "bbbccddd".

def remove_char(s1,s2):
    res = ""
    c = [i for i in s1 if i not in s2]
    for i in c:
        res+=i
    return res

print(remove_char("abccdcdcd","ab"))