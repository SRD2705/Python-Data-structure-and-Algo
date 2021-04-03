'''
Sieve of Eratosthenes
'''


n = int(input())
prime = [True for i in range(n+1)]
p = 2
while p*p <= n:
    if prime[p] == True:
        for i in range(p*p,n+1,p):
            prime[i] = False
    p += 1

print(prime)