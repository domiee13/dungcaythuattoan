# hello5423 Đơn giản 100 Điểm
# Giới hạn ký tự: 3000
# Cho một mảng arr được sắp xếp tăng dần. Hãy rút gọn mảng theo những quy tắc sau:

# Nếu các số từ a đến b là liên tiếp thì chuyển thành a->b
# Nếu chỉ có 1 số thỏa mãn thì chỉ cần in ra số đó
# Ví dụ:

# Với arr = [0,1,2,4,5,7]. Đầu ra splitRange(arr) = ["0->2","4->5","7"].
# Giải thích:
# Các số từ 0 đến 2 là liên tiếp thì ra sẽ rút gọn thành 0->2
# Các số từ 4 đến 5 là liên tiếp thì ta sẽ rút gọn thành 4->5
# Đối với số 7 chỉ duy nhất nên ta sẽ in ra 7

def split_range(arr):
    start = 0
    end = 0
    res= []
    arr.append(0)
    for i in range(0,len(arr)-1):
        if arr[i]+1==arr[i+1]:
            end +=1
        elif start!=end:
            res.append(str(arr[start])+"->"+str(arr[end]))
            start = i+1
            end = i+1
        else:
            res.append(str(arr[end]))
            start = i+1
            end = i+1
    print(res)
    return res

split_range([0,2,3,4,6,8,9])