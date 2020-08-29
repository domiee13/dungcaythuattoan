
# Cho bạn một chuỗi là s1. Mỗi một lần biến đổi, bạn có thể chuyển 1 ký tự giống nhau trong s1 thành một ký tự khác, ví dụ như chuyển tất cả ký tự 'a' thành ký tự 'b' và  mỗi ký tự chỉ được chuyển một lần duy nhất. Bạn giúp DAN xác định xem có thể biến đổi chuỗi s1 thành s2 không.

# Ví dụ:

# Với s1 = "xmms" và s2 = "http" thì switchString(s1, s2) = true
# Ta sẽ biến đổi ký tự 'x' --> 'h',  'm' --> 't', 's' --> 'p'.
# Với s1 = "cddb" và s2 = "abcc" thì  switchString(s1, s2) = false
# Không có cách nào để biến đổi cả

#Accepted - de vai loz
def switchString(s1,s2):
    a = [i for i in s1]
    b = [i for i in s2]
    if len(s1)!=len(s2):
        return False
    for i in range(len(a)):
        if a[i]!=b[i]:
            s1 = s1.replace(a[i],b[i])
    print(s1,s2)
    return s1==s2

switchString("aaabbaaccabacd","eeebbeeuuebeug")