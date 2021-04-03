###################################### Shortest Common Super Sequence(Count) ##############################
'''
In this problem given 2 strings and we have to find out shortest supersequence
Supersequence means a string from which we derive both of the input string
we have to print the shortest one.
The largest one is the str1 + str2
if we know that the number of the longest common subsequence that means those are sequentially common
in both strings.
so if we do [(str1+str2)-lcs count] then we find the answer.
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
lcs = dp[n][m]
res = (n+m) - lcs
print(res)