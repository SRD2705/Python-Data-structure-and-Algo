#################################### Minimum number of deletion in a string to make it a palindrome ##########################################
'''
In this problem you are given a string
The solution is if we calculate longest palindromic sequence from the string then
if we subtract the number from the length of the string we can get our answer.

'''

from copy import deepcopy
li1 = list(input())
li2 = deepcopy(li1)
li2.reverse()
n = len(li1)
m = len(li2)

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if li1[i-1] == li2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(n-dp[n][m])
