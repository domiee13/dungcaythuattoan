# How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

# Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

# rot13("EBG13 rknzcyr.") == "ROT13 example.";
# rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"

#My solution
# def rot13(text):
#     rot13 = str.maketrans( 
#     "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
#     "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
#     return str.translate(text,rot13)

print(rot13("EBG13 rknzcyr."))

#best solution
def rot13_bs(mess):
    return mess.encode('rot13')

import string

def rot13(message):
    return message.encode("rot13")

print(rot13_bs("abc"))