# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
def sortByHeight(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==-1 or a[j]==-1:
                continue
            if a[i]>a[j]:
                a[i],a[j] = a[j],a[i]
    return a