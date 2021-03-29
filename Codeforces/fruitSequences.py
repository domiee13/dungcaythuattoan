# F. Fruit Sequences
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Zookeeper is buying a carton of fruit to feed his pet wabbit. The fruits are a sequence of apples and oranges, which is represented by a binary string s1s2…sn of length n. 1 represents an apple and 0 represents an orange.

# Since wabbit is allergic to eating oranges, Zookeeper would like to find the longest contiguous sequence of apples. Let f(l,r) be the longest contiguous sequence of apples in the substring slsl+1…sr.

# Help Zookeeper find ∑nl=1∑nr=lf(l,r), or the sum of f across all substrings.

# Input
# The first line contains a single integer n (1≤n≤5⋅105).

# The next line contains a binary string s of length n (si∈{0,1})

# Output
# Print a single integer: ∑nl=1∑nr=lf(l,r).

# Examples
# inputCopy
# 4
# 0110
# outputCopy
# 12
# inputCopy
# 7
# 1101001
# outputCopy
# 30
# inputCopy
# 12
# 011100011100
# outputCopy
# 156
# Note
# In the first test, there are ten substrings. The list of them (we let [l,r] be the substring slsl+1…sr):

# [1,1]: 0
# [1,2]: 01
# [1,3]: 011
# [1,4]: 0110
# [2,2]: 1
# [2,3]: 11
# [2,4]: 110
# [3,3]: 1
# [3,4]: 10
# [4,4]: 0
# The lengths of the longest contiguous sequence of ones in each of these ten substrings are 0,1,2,2,1,2,2,1,1,0 respectively. Hence, the answer is 0+1+2+2+1+2+2+1+1+0=12.


t = int(input())

def nCount(s):
    s = s.strip("0")
    a = s.split("0")
    b = [len(i) for i in a]
    return max(b)

s = input()
res = 0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        res+=nCount(s[i:j+1])
print(res)