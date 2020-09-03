def restoreString(str, indices):
    d = {}
    res = ""
    for i in range(len(indices)):
        d[indices[i]]= str[i]
    for i in sorted(d.keys()):
        res+=d[i]
    return res 

#Best solution:
def shuffleString(s,indices):
    return ''.join([s[indices.index(counter)] for counter in list(range(len(s)))])
    return ''.join([s[indices.index(i)] for i in range(len(s))])
print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))       