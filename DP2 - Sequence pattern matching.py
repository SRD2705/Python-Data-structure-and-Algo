#################################################### Sequence pattern matching ################################################
'''
We are given two string and we have to find out this sequence is present or not
so we do simple lcs
if the lcs count is equal to the pattern then it matched else not.
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
if n == dp[n][m]:
    print(True)
else:
    print(False)