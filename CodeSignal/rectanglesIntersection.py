# A rectangle with sides parallel to the axes can be written as a pair of opposing vertices' coordinates of this rectangle.

# Find the area of the intersection of two rectangles given in the described format.

# Example

# For a = [0, 0], b = [2, 2], c = [1, 1], and d = [3, 3], the output should be
# rectanglesIntersection(a, b, c, d) = 1.

def rectanglesIntersection(a, b, c, d):
    
    intersection = []

    for i in range(2):
        if a[i] > b[i]:
            t = a[i]
            a[i] = b[i]
            b[i] = t
        if c[i] > d[i]:
            t = c[i]
            c[i] = d[i]
            d[i] = t
        if b[i] < c[i] or d[i] < a[i]:
            return 0
        intersection += [min(b[i], d[i]) - max(a[i], c[i])]

    return intersection[0] * intersection[1]
