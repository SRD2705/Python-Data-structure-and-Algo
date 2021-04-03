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
dp = [[0 for i in range(s+1)] for j in range(n+1)]
for i in range(s+1):
    dp[0][i] = False
for i in range(n+1):
    dp[i][0] = True
# print(dp)
for i in range(1,n+1):
    for j in range(1,s+1):
        if j >= li[i-1]:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-li[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][s])