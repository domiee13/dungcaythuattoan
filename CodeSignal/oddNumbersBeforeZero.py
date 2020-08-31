# Given an array of integers, count the odd numbers before the first (i.e. leftmost) occurrence of zero.

# Example

# For sequence = [1, 2, 3, 0, 4, 5, 6, 0, 1], the output should be
# oddNumbersBeforeZero(sequence) = 2.
def oddNumbersBeforeZero(sequence):
    res = 0
    for i in sequence:
        if i%2!=0:
            res+=1
        if i==0:
            return res