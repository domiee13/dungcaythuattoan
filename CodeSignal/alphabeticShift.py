# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

def alphabeticShift(inputString):

    chars = list(inputString)
    for i in range(len(chars)):
        number = ord(chars[i]) - ord('a')
        number = (number + 1)%26
        chars[i] = chr(number + ord('a'))
    return ''.join(chars)
