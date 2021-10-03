#################### Unbounded Knapsack ########################
'''
The main difference between 0-1 knapsack and unbounded knapsack is
in this knapsack multiple occurrences is allowed.

In 0-1 knap sack we have only two option either we can take the element or
we can ignore it but we do not consider it again in any cases means no repetition allowed

But in Unbounded knapsack we if we take an element once then we can again take it and
when we do not consider an element we never came back to that element again.
we came back to element if it takes previously either we do not consider it again.

the main code change from 0-1 knapsack is very slight.
the change is in 0-1 knapsack if we take the element then we move on to next element
so we do... dp[i][j] = max((val[i-1] + dp[i-1][j-wt[i-1]]), dp[i-1][j])  in 0-1 knapsack
but in unbounded we consider the element again so we write..
dp[i][j] = max((val[i-1] + dp[i][j-wt[i-1]]), dp[i-1][j])

the changed part is,
dp[i-1][j-wt[i-1]]  ------ >  dp[i][j-wt[i-1]]
'''

val = list(map(int, input().split()))
wt = list(map(int,input().split()))
w = int(input())
n = len(val)
dp = [[0 for i in range(w+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif j >= wt[i-1]:
            dp[i][j] = max((val[i-1] + dp[i][j-wt[i-1]]), dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][w])


'''
1 30
1 50
100

10 40 50 70
1 3 4 5
8
'''