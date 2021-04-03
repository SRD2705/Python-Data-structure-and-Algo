################################## Longest Common Subsequesnce(Count)(tabulation) ##########################
'''
In this case we just convert the recursion code to tabulation method
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)
dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if li1[i-1] == li2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])