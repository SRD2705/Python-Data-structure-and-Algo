################################ Rod cutting problem #########################
'''
In this problem you are given a length of a rod, an price array and you have to cut the rod
to get maximum profit.
so it same as a knapsack problem.You have to make a length array from the length.

The similarity of this problem to knapsack is,
n -------> wt
price[] ----> val[]
length[] -----> price[]
n -----> n

It also a unbounded knapsack because we can cut the same size rod multiple time.
There are no variation from unbounded knapsack
'''


n = int(input())
price = list(map(int, input().split()))
length = [i for i in range(1,n+2)]
dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif j >= length[i-1]:
            dp[i][j] = max((price[i-1]+dp[i][j-length[i-1]]), dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][n])

'''
8
1 5 8 9 10 17 17 20

8
3 5 8 9 10 17 17 20
'''