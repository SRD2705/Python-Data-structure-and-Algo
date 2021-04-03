################################## Coin change problem(Minimum number of coin) #####################################
'''
In this problem we are given a array of coin value and a sum
we have to calculate minimum number of coin required to get the sum.
It look same as the subset sum problem but
the initialization is little bit different in it.
if we given a sum 1 or more and coin array is empty then,
mathematically it needs infinite coin to get the sum.
so we initialize with infinite

In this problem we need to initialize the second array.
and in the subset sum we calculate the max but in this case we calculate the min.

and add +1 everytime we consider an element.


'''

import sys
coin = list(map(int, input().split()))
s = int(input())
n = len(coin)
dp = [[0 for i in range(s+1)] for j in range(n+1)]
for i in range(s+1):
    dp[0][i] = sys.maxsize
for i in range(1, s+1):
    if i % coin[0] == 0:
        dp[1][i] = i // coin[0]
    else:
        dp[1][i] = sys.maxsize
for i in range(2,n+1):
    for j in range(1,s+1):
        if j >= coin[i-1]:
            dp[i][j] = min((dp[i][j-coin[i-1]])+1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][s])
