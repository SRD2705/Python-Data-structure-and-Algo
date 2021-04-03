#################################################### Minimum number of insertion in a string to make it a palindrome ########################################
'''
this problem is similar to the deletion problem.
basically we delete single elements and to make palindrome we have to
add the same element to make it a pair.
so number of deletion and the number of insertion is same.
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
        if li1[i-1]==li2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(n-dp[n][m])
