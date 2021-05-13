prime = [0] * 100001
k = [0] * 100001

def Sieve():
    for i in range(1, 100001):
        k[i] = i

    for i in range(2, 100001):

        # If i is prime then remove all
        # factors of prime from it
        if (prime[i] == 0):
            for j in range(i, 100001, i):

                prime[j] = 1

                while (k[j] % (i * i) == 0):
                    k[j] /= (i * i)

def countPairs(arr, n):
    freq = dict()

    for i in range(n):
        if k[arr[i]] in freq.keys():
            freq[k[arr[i]]] += 1
        else:
            freq[k[arr[i]]] = 1

    Sum = 0
    for i in freq:
        Sum += (freq[i] * (freq[i] - 1)) / 2

    return Sum


arr = [8,2]

# Length of arr
n = len(arr)

# To pre-compute the value of k
Sieve()

# Function that return total count 
# of pairs with perfect square product 
print(int(countPairs(arr, n)))