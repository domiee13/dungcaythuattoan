# Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

# Note, that during capitalization all the letters except the first one remains unchanged.

s = input()
a = [i for i in s]

a[0] = a[0].upper()
print("".join(a))
