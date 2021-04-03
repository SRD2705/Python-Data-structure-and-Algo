############################ Longest palindromic subsequence(Count) ######################
'''
In this problem you are given a string and you have to calculate longest palindromic sequence count.
So it seems like it is no match to the lcs problem but you know the key characteristics of palindrome.
so we get a input and another if reverse of the string.
For example,
s = 'agbcba'
so after reverse
s1 = 'abcbga'

now if you look closely if you get the lcs from both the string it will give you the
longest common palindromic subsequence.

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
print(dp[n][m])