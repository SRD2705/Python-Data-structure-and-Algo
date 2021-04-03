################################## Longest Common Substring ############################
'''
In this problem we are given two string and print the count of longest substring
difference between substring and subsequence is subsequence can be discrete but
substring must be contagious.

So the basic change is when the character does not match we set the counter to zero
and return the max value in the dp table.
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)

dp = [[0 for i in range(m+1)] for j in range(n+1)]
res = 0
for i in range(n+1):
    for j in range(m+1):
        if li1[i-1] == li2[j-1]:
            dp[i][j] = 1+dp[i-1][j-1]
            if dp[i][j] > res:
                res = dp[i][j]
        else:
            dp[i][j] = 0
print(res)