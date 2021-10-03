############################ Minimum subset sum difference ##################################
'''
In this problem you have to find out the minimum subset sum difference
It is similer to the subset sum problem but the difference is in subset sum difference
we can check the given sum if possible or not. and the dp table is boolean
but in this case we have to modify a bit.
Here we are given a array only so we can find a range and the extreme difference is (0,sum(li)
so we find the range.Then we have to do subset sum and get the boolean dp table
The main result we need is the last row of the table because here we can see which sum are possible with this array
so we just take the possible numbers in an array(which are TRUE in the last row)
then using a single loop we can calculate the minimum difference of the subsets.

if one number is s1 then another must be (s-s1)
so the difference is (s-s1)-s1 = s - 2s1
s1 are stores in the res here
'''
import sys
def subsetsumpos(li,s):
    n = len(li)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    res = 0
    for i in range(s+1):
        dp[0][i] = False
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if j >= li[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-li[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    for i in range(s//2,-1,-1):
        if dp[n][i] == True:        # Traversing the last row to get the possible numbers
            res = s - (2*i)
    return res

li = list(map(int, input().split()))
s = sum(li)
res = subsetsumpos(li,s)
print(res)