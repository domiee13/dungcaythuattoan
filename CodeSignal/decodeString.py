# Given an encoded string, return its corresponding decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

# Note that your solution should have linear complexity because this is what you will be asked during an interview.

# Example

# For s = "4[ab]", the output should be
# decodeString(s) = "abababab";

# For s = "2[b3[a]]", the output should be
# decodeString(s) = "baaabaaa";

# For s = "z1[y]zzz2[abc]", the output should be
# decodeString(s) = "zyzzzabcabc".

import collections
def decodeString(s):
    res = []
    idx = len(s)-1
    
    while idx>=0:
        i = s[idx]
        
        if i.isdigit():
            d = i
            while idx-1>=0 and s[idx-1].isdigit():
                d += s[idx-1]
                idx -= 1
            d = int(d[::-1])
            
            t = ""
            while res:
                temp = res.pop()
                if temp == ']': break
                t += temp
                
            res.append(t * d)
             
        elif i!='[':
            res.append(i)
        
        idx -= 1
    return "".join(res[::-1])
    