# lamvh Đơn giản 100 Điểm
# Giới hạn ký tự: 3000
# Nâm rất thích uống Coca. Trên đường đi học về cậu gặp một cửa hàng có chương trình đổi y vỏ chai lấy 1 chai nguyên. Nhưng cậu chỉ có tiền mua được x chai coca. Hãy giúp Nâm tính xem từ x chai nguyên ban đầu đó thì cậu sẽ được uống bao nhiêu chai coca.

# Ví dụ:

# Với x = 15, y = 4 thì numCoca(x, y) = 19. Vì ban đầu Nâm có 15 chai coca. Sau khi uống hết 15 chai đó, Nâm đổi được thêm được 3 chai Coca mới và còn lại 3 vỏ chai. rồi Nâm đổi thêm được 1 chai Coca nữa và còn thừa lại 2 vỏ chai. Cuối cùng Nâm không đổi được nữa. Tổng cộng là 15 + 3 + 1 = 19.
# Với x  = 2, y = 3 thì numCoca(x, y) = 2. Nâm uống 2 chai coca xong thì không đổi được vỏ chai.

def numCoca(x,y):
    res = x
    while x>=y:
        res+=x//y
        x = x//y + x%y
    return res