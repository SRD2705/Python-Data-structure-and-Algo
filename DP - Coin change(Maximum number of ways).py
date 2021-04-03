############################ Coin change problem(Maximum number of ways) ###########################
'''
In this problem we are given an array of coin value and a sum.
we have to find out number of ways we can achieve the target
Clearly it is similar to the subset sum problem and we can use the same problem
multiple time so it is unbounded.

So it is basically unbounded subset sum.
the change is i(for unbounded) & i-1(for 0-1)

'''

coin = list(map(int, input().split()))
s = int(input())
n = len(coin)
dp = [[0 for i in range(s+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1,n+1):
    for j in range(1,s+1):
        if j >= coin[i-1]:
            dp[i][j] = dp[i-1][j] + dp[i][j-coin[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][s])
