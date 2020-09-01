# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case. (Use the English alphabet with 26 letters!)

# Examples:

# If array = ["a","b","c","d","f"] then missingLetter = "e"
# If array = ["O","Q","R","S"] then missingLetter = "P"

def find_missing_letter(array):
    d = []
    for i in range(len(array)):
        d.append(ord(array[i]))
    d = sorted(d)
    for i in range(len(d)-1):
        if d[i+1]-d[i]==2:
            return chr(d[i]+1)