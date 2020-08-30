# Given a sequence determine if it's a geometric progression or not.

# Example

# For sequence = [1, 4, 16], the output should be
# isGeometricProgression(sequence) = true;
# For sequence = [2, 4, 8, 17, 34], the output should be
# isGeometricProgression(sequence) = false.

def isGeometricProgression(sequence):
    a = []
    for i in range(len(sequence)-1):
        a.append(sequence[i+1]/sequence[i])
    return len(set(a))==1
