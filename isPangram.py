# Một pangram là một câu mà mỗi kí tự chữ cái (a-z) được sử dụng ít nhất một lần

# Cho một xâu kí tự, kiểm tra xem nó có phải là một pangram hay không?

# Ví dụ:

# Với sentence = "The quick brown fox jumps over the lazy dog.", thì kết quả isPangram(sentence) = true;
# Với sentence = "abcdefghijklmnopqrstuvwxya", thì kết quả isPangram(sentence) = false.

def isPangram(sentence):
    a = sentence.split(" ")
    sentence = "".join(a)
    b = [i.lower() for i in sentence if i.isalpha()]
    print(b)
    b = set(b)
    print(len(b))
    if len(b)==26:
        return True
    return False

isPangram("The quick brown fox jumps over the lazy dog.")