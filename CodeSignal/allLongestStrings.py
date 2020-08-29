# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    tmp = max([len(i) for i in inputArray])
    res = [i for i in inputArray if len(i)==tmp]
    return res

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))