# Trong giấc mơ, bạn đang ở một hành tinh nào đó. Trước mặt bạn là đám trẻ xếp thành một hàng, chìa tay sẵn sàng nhận kẹo từ bạn, bạn phải đảm bảo rằng mỗi đứa trẻ phải được nhận ít nhất 1 cây kẹo. Nếu có hai đứa trẻ đứng cạnh nhau nhưng độ tuổi khác nhau thì đứa lớn hơn phải được chia nhiều hơn. Vì xót thương cho cái hầu bao của mình nên bạn phải tính toán kĩ càng làm sao mua ít kẹo nhất có thể nhưng vẫn chia đủ cho tất cả.

# Ví dụ: 

# Với age=[4, 6, 5, 6, 7, 2], thì distributeCandy(age)=10.
# Đám trẻ sắp thành hàng có độ tuổi là [4, 6, 5, 6, 7, 2]. Bạn phải đưa ít nhất số kẹo như sau: [1, 2, 1, 2, 3, 1]. Vậy bạn phải mua ít nhất 10 cây kẹo.

#Fixing . . . 
def distributeCandy(age):
    tmp = 1
    res = []
    tmp = {}
    tmp[age[0]] =1
    res.append(1)
    for i in range(1,len(age)):
        if age[i]>age[i-1]:
            tmp[age[i]] = tmp[age[i-1]]+1
            res.append(tmp[age[i-1]]+1)
        else:
            tmp[age[i]] = tmp[age[i-1]]-1
            res.append(tmp[age[i-1]]-1)
    print(res)
distributeCandy([4, 6, 5, 6, 7, 2])