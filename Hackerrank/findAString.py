# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

def count_substring(string, sub_string):
    # return string.count(sub_string)
    res = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            res+=1
    return res