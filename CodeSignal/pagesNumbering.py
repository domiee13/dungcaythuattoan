# Given a number of the pages in some book find the number of digits one needs to print to enumerate the pages of the book.

# Example

# For n = 11, the output should be
# pagesNumbering(n) = 13.
def pagesNumbering(n):
    res = 0
    for i in range(1,n+1):
        res += len(str(i))
    return res