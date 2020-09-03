# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

def calScore(str):
    res = 0
    for i in str:
        res += ord(i)-96
    return res
def high(x):
    # Code here
    res = x.split()[0]
    max = calScore(x.split()[0])
    for i in x.split():
        if max<calScore(i):
            max = calScore(i)
            res = i
    return res

def high1(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))