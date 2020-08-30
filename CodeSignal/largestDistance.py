# You are given a set of points on the Cartesian plane. Consider the distance between two points as the maximum difference of their coordinates. For example, the distance between points (1, 2) and (4, 6) is equal to max(|4 - 1|, |6 - 2|) = 4.

# Given a set of points, find the pair with the largest distance and return the value of their distance.

# Example

# For a = [7, 6, 6, 8, 1, 2, 8, 6], the output should be
# largestDistance(a) = 7.

def largestDistance(a):
    
    mx = [a[0], a[1]]
    mn = [a[0], a[1]]
    for i in range(len(a)):
        k = i % 2 #?????
        if a[i] > mx[k]:
            mx[k] = a[i]
        elif a[i] < mn[k]:
            mn[k] = a[i]
    return max(mx[0] - mn[0], mx[1] - mn[1])
