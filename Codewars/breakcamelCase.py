# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# solution("camelCasing")  ==  "camel Casing"

def solution(s):
    idx = []
    idx.append(0)
    res= ""
    for i in range(len(s)):
        if s[i].isupper():
            idx.append(i)
    idx.append(len(s))
    for i in range(len(idx)-1):
        res += s[idx[i]:idx[i+1]]+" "
    print(res)
    return res.strip()
solution("breakCamelCase")

#Another solution
def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
