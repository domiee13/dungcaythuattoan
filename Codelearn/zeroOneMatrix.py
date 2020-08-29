# Cho ma trận mat có kích thước nxm chỉ bao gồm số 0 và 1.

# Nếu giá trị mat[i][j]=1 (với 0≤i≤n, 0≤j≤m) thì ma trận được biến đổi sao cho các giá trị ở hàng thứ i và cột thứ j đều chuyển thành 1.

# Trả về ma trận sau khi đã thực hiện phép biến đổi, nếu không thể thực hiện phép biến đổi thì trả về trạng thái hiện tại của ma trận.

def zeroOne(mat):
    iArray = []
    jArray = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]==1:
                iArray.append(i)
                jArray.append(j)
    res = mat.copy()
    for i in range(len(res)):
        for j in range(len(res[i])):
            if i in iArray or j in jArray:
                res[i][j]=1
    return res