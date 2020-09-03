# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

def iq_test(numbers):
    #your code here
    odd = []
    even = []
    numbers = numbers.split()
    for i in numbers:
        if int(i)%2!=0:
            odd.append(i)
        else:
            even.append(i)
    if len(odd)==1:
        return numbers.index(odd[0])+1
    else:
        return numbers.index(even[0])+1
#Another solution
def iq_test1(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1