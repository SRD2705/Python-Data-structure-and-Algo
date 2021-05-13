######################################### Print shortest common Supersequence ################################################
'''
In this problem you are given two string
we already know how to get count of shortest common supersequence.
we also know hoe to print longest common subsequence.

in lcs printing if both letter math we append it to the result but in this case if not match we must include the letter too
an another change is we break loop when i or j reaches 0 but there are few letters left because if i is 0 that means j is not 0 and vice-versa

Remember the worst case of supersequence is (string1+string2)

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
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[n][m])
# print((n+m - dp[n][m]))

i = n
j = m
res = []
while i>0 and j>0:
    if li1[i-1] == li2[j-1]:
        res.append(li1[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i][j-1] > dp[i-1][j]:
            res.append(li2[j-1])
            j -= 1
        else:
            res.append(li1[i-1])
            i -= 1
while i > 0:
    res.append(li1[i-1])
    i -= 1
while j > 0:
    res.append(li2[j-1])
    j -= 1
res.reverse()
print(*res,sep='')