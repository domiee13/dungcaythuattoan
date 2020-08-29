# Mã Morse hay mã Moóc-xơ dùng một chuỗi đã được chuẩn hóa gồm các phần tử ngắn  và dài  để biểu diễn một thông điệp.

# Thầy Hải là tổng phụ trách Đội ở một trường Tiểu học, đang dạy cho các học sinh về truyền tin Morse, theo đó thầy Hải sẽ thổi còi để các học sinh theo tín hiệu chép lại thông tin.

# Tiếng còi ngắn biểu diễn cho phần tử ngắn  
# Tiếng còi dài biểu diễn cho phần tử dài 
# Trong tay thầy đang có một chuỗi message, hãy giúp thầy tính số phần tử ngắn  và số phần tử dài  cần thổi, biết rằng:

# Số tiếng còi là tối thiểu để truyền đạt thông tin trên chuỗi message và không truyền đạt dấu khoảng trắng.
# Chuỗi message chỉ chứa dấu khoảng trắng và các kí tự biểu diễn được trong bảng mã morse (không chứa các kí tự viết thường và các kí tự có dấu)
# Khi bắt đầu truyền tin và kết thúc truyền tin luôn có hiệu còi bắt đầu () và kết thúc ()

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
# Hieu coi bat dau .-.-.-
# Hieu coi ket thuc .-.-.
def textToMorse(s):
    res = ""
    for i in s:
        res+=MORSE_CODE_DICT[i]
    return res

def morseCode(message):
    content = ""
    for i in message.split():
        content = content + " " + textToMorse(i)
    res1 = content.count('.')+6
    res2 = content.count('-')+5
    return [res1,res2]

print(morseCode("WAKANDA FOREVER"))