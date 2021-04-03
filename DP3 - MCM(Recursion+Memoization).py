############################################## MCM(Recursion+Memoization) ###################################################
'''
Since same suproblems are called again, this problem has Overlapping Subprolems property.
So Matrix Chain Multiplication problem has both properties (see this and this) of a dynamic programming problem.
Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by
constructing a temporary array m[][] in bottom up manner.
'''

import sys
def mcm(li,i,j):
    global dp
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        res = sys.maxsize
        for k in range(i,j):
            tmp = mcm(li,i,k) + mcm(li,k+1,j) + (li[i-1]*li[k]*li[j])
            res = min(res, tmp)
        dp[i][j] = res
        return res

li = list(map(int, input().split()))
n = len(li)
dp = [[-1 for i in range(n+1)] for j in range(n+1)]
res = mcm(li,1,n-1)
print(res)
# print(dp)
