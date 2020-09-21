# VuTungMinh Đơn giản 100 Điểm
# Giới hạn ký tự: 3000
# Bạn là một chủ cửa hàng vớ (tất) vừa mới nhập về một lô hàng sizes có các loại vớ có size khác nhau, nhưng vì một số lý do bất khả kháng mà lô hàng vừa nhập về lại bị lẫn lộn các size với nhau. Để bán được hàng, bạn buộc phải biết được số đôi vớ có size bằng nhau mà lô hàng vừa rồi nhập về nàm trong 1 mảng sizes, hãy cho biết có bao nhiêu đôi trong số hàng đó.

# Ví dụ: 

# Với sizes = [1, 2, 1, 2, 1, 3, 2] thì sock_merchant(sizes) = 2
# Giải thích: có 1 đôi vớ có size 1 và 1 đôi vớ có size 2, còn lại không có đôi vớ nào có size bằng nhau.

def sock_merchant(sizes):
    s = set(sizes)
    a = []
    for i in s:
        a.append(sizes.count(i)//2)
    print(a)
    return sum(a)

sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])

#Rut gon
def sock_merchant1(sizes):
    return sum([sizes.count(i)//2 for i in set(sizes)])