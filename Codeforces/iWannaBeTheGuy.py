# A. I Wanna Be the Guy
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# There is a game called "I Wanna Be the Guy", consisting of n levels. Little X and his friend Little Y are addicted to the game. Each of them wants to pass the whole game.

# Little X can pass only p levels of the game. And Little Y can pass only q levels of the game. You are given the indices of levels Little X can pass and the indices of levels Little Y can pass. Will Little X and Little Y pass the whole game, if they cooperate each other?

# Input
# The first line contains a single integer n (1 ≤  n ≤ 100).

# The next line contains an integer p (0 ≤ p ≤ n) at first, then follows p distinct integers a1, a2, ..., ap (1 ≤ ai ≤ n). These integers denote the indices of levels Little X can pass. The next line contains the levels Little Y can pass in the same format. It's assumed that levels are numbered from 1 to n.

# Output
# If they can pass all the levels, print "I become the guy.". If it's impossible, print "Oh, my keyboard!" (without the quotes).

# Examples
# inputCopy
# 4
# 3 1 2 3
# 2 2 4
# outputCopy
# I become the guy.
# inputCopy
# 4
# 3 1 2 3
# 2 2 3
# outputCopy
# Oh, my keyboard!

n = int(input())

a = list(set([int(i) for i in input().split()]))
b = list(set([int(i) for i in input().split()]))

ok = True
for i in range(1,n+1):
    if i not in a and i not in b:
        ok = False
        break
if ok:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")