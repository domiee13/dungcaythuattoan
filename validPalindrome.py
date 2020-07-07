# Cho một chuỗi s bạn hãy kiếm tra xem s có phải là chuỗi đối xứng không. Và chúng ta chỉ xét đối xứng với các chữ cái, số và không phân biệt in hoa hay thường

# Biết rằng chuỗi đối xứng là chuỗi khi viết từ trái qua phải, cũng giống như khi viết từ phải qua trái.

# Ví dụ:

# Với s = "code*@e do(c" thì kết quả valid_palindrome(s) = True

# Giải thích:
# Vì ta chỉ xét với các chữ cái, số nên s có thể viết lại là "codeedoc"
# Và "codeedoc" chính là chuỗi đối xứng, nên kết quả là True

def valid_palindrome(s):
    a =[str(i).lower() for i in s if str(i).isdigit() or str(i).isalpha()]
    print(a)
    return a==a[::-1]

valid_palindrome("A man, a plan, a canal: Panama"
)
print(valid_palindrome("A man, a plan, a canal: Panama"
))