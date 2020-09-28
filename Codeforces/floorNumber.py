# A. Floor Number
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Vasya goes to visit his classmate Petya. Vasya knows that Petya's apartment number is .

# There is only one entrance in Petya's house and the distribution of apartments is the following: the first floor contains  apartments, every other floor contains  apartments each. Apartments are numbered starting from one, from the first floor. I.e. apartments on the first floor have numbers  and , apartments on the second floor have numbers from  to , apartments on the third floor have numbers from  to , and so on.

# Your task is to find the number of floor on which Petya leaves. Assume that the house is always high enough to fit at least  apartments.

# You have to answer  independent test cases.

# Input
# The first line of the input contains one integer  () — the number of test cases. Then  test cases follow.

# The only line of the test case contains two integers  and  () — the number of Petya's apartment and the number of apartments on each floor of the house except the first one (there are two apartments on the first floor).

# Output
# For each test case, print the answer: the number of floor on which Petya lives.

import math
t = int(input())

for i in range(t):
    n,x = map(int,input().split())
    if n==1 or n==2:
        print(1)
    else:
        print(math.ceil((n-2)/x)+1)

# def find(n,x):
#     if n==1 or n==2:
#         return 1
#     else:
#         res = 3
#         i = 2
#         while res!=n:
#             res+=x
#             i+=1
#         return i
# print(find(987,13))