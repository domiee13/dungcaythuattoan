s = "−−−−− −− ••−−•− •••−− •−• −••• ••− •−•• −•−• •−−• ••• ••"
s = s[::-1]

print(s)

a = []
for i in s.split():
    a.append(i[::-1])
print(" ".join(a))

