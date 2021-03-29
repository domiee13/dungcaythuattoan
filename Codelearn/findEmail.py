# Một email có cấu trúc như sau <tên đăng nhập>@<tên miền>. Trong đó:
# Tên đăng nhập:

# Chỉ chứa các chữa cái(a-z,A-Z) ,số(0-9) và dấu chấm(.). Không chứa nhiều dấu chấm liên tiếp.
# Không bắt đầu hoặc kết thúc bằng dấu chấm.
# Tên miền gồm: <tên>.<hậu tố> :

# Tên hậu tố chỉ bao gồm các ký tự trong bảng chữ cái (a-z,A-Z), các số (0-9) và dấu trừ (-).
# Không thể bắt đầu bằng hoặc kết thúc tên miền bằng dấu trừ (-).
# Cho chuỗi s chứa các từ được ngăn cách nhau bằng khoảng trắng. Hãy tìm 1 từ là 1 email xuất hiện đầu tiên trong s, nếu không tìm thấy trả về "Not found!".

# Ví dụ:

# Với s="abc123@gmail.com" thì findEmail(s)="abc123@gmail.com".
# Với s="Moi thong tin chi tiet vui long lien he: thien1082004vn@gmail.com" thì findEmail(s)="thien1082004vn@gmail.com".
# Import regex module
import re

def findEmail(s):
    x = re.search("([a-zA-Z0-9]+@gmail.com)",s)
    print(s[x.start():x.end()])
test = "Moi thong tin chi tiet vui long lien he: thien1082004vn@gmail.com"
findEmail(test)
#??
# Đầu vào:"2323adjv ncdj fbejs dcbh ncncnvnv.vcsaxs.x.x.x.x.x.a.a.a@gg.v"
# Đầu ra thực tế:"a@gg.v"
# Đầu ra mong muốn:"ncncnvnv.vcsaxs.x.x.x.x.x.a.a.a@gg.v"

# import re

# def findEmail(s):
#     x = re.search("([a-zA-Z0-9]+@[a-z]+.[a-z]+)",s)
#     if(x):
#         return (s[x.start():x.end()])
#     return "Not found!"