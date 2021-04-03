###################Subset sum possible(T or F)##################
'''
This is a program for calculating if subset sum possible or not
we use dp and iteration in this
We initialize dp with T and F
is sum is 0 then we can make 0 from any length of array
because we know empty array is also a subset
'''

li = list(map(int, input().split()))
s = int(input())
n = len(li)
d = [[0 for i in range(s+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            d[i][j] = False
        if j == 0:
            d[i][j] = True
for i in range(1,n+1):
    for j in range(1,s+1):
        if li[i-1] < s:
            d[i][j] = d[i][j-li[i-1]] or d[i-1][j]
        else:
            d[i][j] = d[i-1][j]
print(d[n][s])