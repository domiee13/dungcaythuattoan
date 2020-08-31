# You are given two positive integers a and b. If you write them down next to each other on a piece of paper with no space between them, you'll get a new number. Return that number.

# Example

# For a = 23 and b = 45, the output should be
# concatenateNumbers(a, b) = 2345.

def concatenateNumbers(a, b):
    tmp = b

    while tmp != 0:
        tmp //= 10
        a *= 10

    return a + b
