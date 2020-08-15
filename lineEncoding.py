# Cho một xâu kí tự, viết hàm mã hóa xâu đó theo các luật sau:

# Đầu tiên, cắt xâu ban đầu thành các xâu con mà mỗi xâu con chỉ chứa các kí tự giống nhau và xâu con tạo ra có độ dài là lớn nhất
# Ví dụ, xâu "aabbbc" được tách thành ["aa", "bbb", "c"]
# Tiếp theo, với mỗi xâu con có chiều dài lớn hơn 1, hãy thay thế xâu đó bằng việc viết liền độ dài của xâu với kí tự lặp lại
# Ví dụ, xâu con "bbb" được thay thế bằng "3b"
# Cuối cùng, viết liên tiếp các xâu con vừa được mã hóa theo thứ tự ban đầu để tạo ra xâu kết quả
# Ví dụ:

# Với s = "aabbbc", thì kết quả lineEncoding(s) = "2a3bc".

def lineEncoding(s):
    res = ""
    tmp = ""
    a = []
    string = [i for i in s]
    for i in range(len(string)):
        if tmp!='':
            if string[i]==tmp[0]:
                tmp+=string[i]
            else:
                a.append(tmp)
                tmp = ""
                tmp+=string[i]
        if tmp=='':
            tmp+=string[i]
    a.append(tmp)
    c=[]
    for i in a:
        c.append(len(i))
    for i in range(len(a)):
        if c[i]>1:
            res+= str(c[i])+a[i][0:1]
        else:
            res += a[i][0:1]
    return res

print(lineEncoding("abbcabb"))