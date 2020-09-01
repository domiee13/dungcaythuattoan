# Cho một dãy gồm các số tự nhiên từ 1 đến n, hãy tính số các số chẵn thuộc dãy trên và chia hết cho k.

# Ví dụ:

# Với n = 7, k = 3 thì numOfEven(n, k) = 1 
#      Giải thích: Ở dãy trên thì chỉ có 6 là số chẵn chia hết cho 3.

# Với n = 24, k = 5 thì numOfEven(n, k) = 2 

def numOfEven(n,k):
    return n//k if k%2==0 else n//(2*k)