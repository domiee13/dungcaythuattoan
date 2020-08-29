# Halley có thói quen đặt mật khẩu bằng các số. Mật khẩu gần đây cậu đặt cho tài khoản Facebook là n với n là một số nguyên dương. Một thời gian cậu phát hiện ra rằng, Cortana đang dò mật khẩu Facebook của mình. Halley quyết định thay đổi mật khẩu theo quy tắc sau: Cậu chọn ra một số nguyên dương a nhỏ nhất sao cho a chia hết cho n và a có k hoặc nhiều hơn k số 0 ở cuối số (k là số nguyên dương). Bạn hãy giúp Halley tìm ra số thỏa mãn nhé.

n,k = input().split(" ")

n,k = int(n),int(k)

a = str(n)+'0'*k
a = int(a)

print(a)
