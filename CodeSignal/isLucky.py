# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

def isLucky(n):
    if len(str(n))%2!=0:
        return False
    a = [int(i) for i in str(n)]     
    front = a[:len(a)//2]
    back = a[len(a)//2:]
    return sum(front)==sum(back)

print(isLucky(1230))