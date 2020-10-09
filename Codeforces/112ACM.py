# You are given natural numbers a and b. Find a^b-b^a.
# ae8dc93c44f6887c0dd9369f6b8b2aa60b7e9da8b0b6df87adda97d6d82eaab8

a,b = input().split(" ")
a,b = int(a),int(b)

print(a**b-b**a)