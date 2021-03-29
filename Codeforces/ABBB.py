t = int(input())

for i in range(t):
    s = input()
    while(len(s)!=0):
        if "AB" in s:
            s = s.replace("AB",'')
        elif "BB" in s:
            s = s.replace("BB",'')
        else:
            break
    print(len(s))