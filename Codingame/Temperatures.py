import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
am = []
duong = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t>0:
        duong.append(t)
    elif t<0:
        am.append(t)
res = 0
if len(duong)==0:
    res = max(am)
elif len(am)==0:
    res = min(duong)
elif len(duong)==0 and len(am)==0:
    res = 0
elif 0-max(am)<min(duong)-0:
    res = max(am)
else:
    res = min(duong)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(res)
