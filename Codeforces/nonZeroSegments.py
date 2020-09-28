#WA
# D. Non-zero Segments
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Kolya got an integer array . The array can contain both positive and negative integers, but Kolya doesn't like , so the array doesn't contain any zeros.

# Kolya doesn't like that the sum of some subsegments of his array can be . The subsegment is some consecutive segment of elements of the array.

# You have to help Kolya and change his array in such a way that it doesn't contain any subsegments with the sum . To reach this goal, you can insert any integers between any pair of adjacent elements of the array (integers can be really any: positive, negative, , any by absolute value, even such a huge that they can't be represented in most standard programming languages).

# Your task is to find the minimum number of positive integers you have to insert into Kolya's array in such a way that the resulting array doesn't contain any subsegments with the sum .

# Input
# The first line of the input contains one integer  () — the number of elements in Kolya's array.

# The second line of the input contains  integers  () — the description of Kolya's array.

# Output
# Print the minimum number of integers you have to insert into Kolya's array in such a way that the resulting array doesn't contain any subsegments with the sum .

# Examples
# inputCopy
# 4
# 1 -5 3 2
# outputCopy
# 1
# inputCopy
# 5
# 4 -2 3 -9 2
# outputCopy
# 0
# inputCopy
# 9
# -1 1 -1 1 -1 1 1 -1 -1
# outputCopy
# 6
# inputCopy
# 8
# 16 -5 -11 -15 10 5 4 -4
# outputCopy
# 3
# Note
# Consider the first example. There is only one subsegment with the sum . It starts in the second element and ends in the fourth element. It's enough to insert one element so the array doesn't contain any subsegments with the sum equal to zero. For example, it is possible to insert the integer  between second and third elements of the array.

# There are no subsegments having sum  in the second example so you don't need to do anything.

n = int(input())

a = [int(i) for i in input().split()]
res = 0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if sum(a[i:j+1])==0:
            res +=1
print(res)