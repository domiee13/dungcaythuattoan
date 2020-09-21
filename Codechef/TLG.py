#wrong answer
# Input

# The first line of the input will contain a single integer N (N ≤ 10000) indicating the number of rounds in the game. Lines 2,3,...,N+1 describe the scores of the two players in the N rounds. Line i+1 contains two integer Si and Ti, the scores of the Player 1 and 2 respectively, in round i. You may assume that 1 ≤ Si ≤ 1000 and 1 ≤ Ti ≤ 1000.

# Output

# Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and indicates the winner and L is the maximum lead attained by the winner.

# Example

# Input:

# 5
# 140 82
# 89 134
# 90 110
# 112 106
# 88 90
# Output:

# 1 58

t = int(input())
sc = []#Score
player = []
for i in range(t):
    a,b = map(int,input().split())
    sc.append(abs(a-b))
    if a>b:
        player.append(1)
        # a1+=a
    else:
        player.append(2)
        # a2+=b   
print(player[sc.index(max(sc))],max(sc))