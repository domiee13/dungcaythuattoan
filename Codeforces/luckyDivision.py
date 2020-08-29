# Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.
#
# Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.
#
# Input
# The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.
#
# Output
# In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes)

check = [4, 7, 47, 74, 44, 444, 447, 474, 477, 777, 774, 744]


def luckyCheck(n):
    for i in check:
        if n % i == 0:
            return "YES"
    return "NO"


n = int(input())
print(luckyCheck(n))
