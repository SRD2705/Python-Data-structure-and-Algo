############################## Min number of insertion and deletion to convert string A to B ######################
'''
In this problem we have to calculate the number of insertion and deletion to convert string a to b.
so lcs gives us the count of sequentially common sequence
that means number of lcs is present in both string
so we need to delete len(a) - lcs
ans insert len(b) - lcs
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if li1[i-1] == li2[j-1]:
            dp[i][j] = 1+ dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# print(dp[n][m])
tmp = dp[n][m]
ins = m - tmp
delt = n-tmp
print(ins,delt)