################################################################ Palindrome Partition(Recursion+Memoization+Optimize) ######################################################################################
'''
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome.
For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.
Determine the fewest cuts needed for a palindrome partitioning of a given string.
For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”.
If a string is a palindrome, then minimum 0 cuts are needed.
If a string of length n containing all different characters, then minimum n-1 cuts are needed.
we use dp[][] to store the value
If the recursion is calculated previously then return the value else call the recursion.
More optimization is when we call the two recursion we check those in the dp table.
'''


import sys
def ispalin(s):
    return s == s[::-1]

li = list(input())
n = len(li)
dp = [[-1 for i in range(n+1)] for j in range(n+1)]

def pal_part(s,i,j):
    if i>=j or ispalin(s[i:j+1]):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    res = sys.maxsize
    for k in range(i,j):
        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = pal_part(s,i,k)
        if dp[k+1][j] != -1:
            right = dp[k+1][j]
        else:
            right = pal_part(s,k+1,j)
        tmp = 1 + left + right
        res = min(res, tmp)
    dp[i][j] = res
    return res

print(pal_part(li,0,n-1))
