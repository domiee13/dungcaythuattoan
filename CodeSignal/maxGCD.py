# For a given set of positive integers remove one of them to maximize the greatest common divisor (GCD) of the remaining integers. Return the maximized GCD.

# Example

# For sequence = [8, 60, 12, 3], the output should be
# maxGCD(sequence) = 4.

# The best option is to remove the element 3, so that gcd([8, 60, 12]) = 4.

def maxGCD(sequence):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    bestRes = 0

    for i in range(len(sequence)):
        result = sequence[0]
        if i == 0:
            result = sequence[1]
        for j in range(len(sequence)):
            if i == j:
                continue
            result = gcd(result, sequence[j])
        if result > bestRes:
            bestRes = result

    return bestRes
