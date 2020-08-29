# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# reverseInParentheses(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# reverseInParentheses(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# reverseInParentheses(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# reverseInParentheses(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

def reverseInParentheses(s):
    res = "" 
    tmp = ""
    checked = []
    for i in range(len(s)):
        if i not in checked:
            if s[i]!='(':
                res+=s[i]
            else:
                while s[i]!=')':
                    tmp+=s[i]
                    checked.append(i)
                    i+=1
                res += tmp[::-1]
                tmp = ""
    res = res.replace('(','')
    res = res.replace(')','')
    print(res)

reverseInParentheses("(bar)(dom)")