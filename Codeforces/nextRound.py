# A. Next Round
# time limit per test3 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# "Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

# A total of n participants took part in the contest ( n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.

# Input
# The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

# The second line contains n space-separated integers a 1, a 2, ..., a n (0 ≤ a i ≤ 100), where a i is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: a i ≥ a i + 1).

# Output
# Output the number of participants who advance to the next round.

n,k = input().split(" ")
n,k = int(n),int(k)

s = input().split(" ")
a = [int(i) for i in s]

tmp = a[k-1]
res = [i for i in a if i > 0 and i >= tmp]
print(len(res))