######################################## Longest Common Subsequence(Print any) #############################################
'''
In this problem we have to print longest common subsequence.
In previous problem we count the length of the lcs and print it.
In this problem we create the same dp table then backtrack it.

we start from the last.(i==n,j==m)
If we found the match then we append the element to the result and decrement both i,j
else we move to the upper of left maximum.
reverse the result and print the result.
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)
res = []
dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if li1[i-1] == li2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

i = n
j = m
while i > 0 and j >0:
    if li1[i-1] == li2[j-1]:
        res.append(li1[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i][j-1] > dp[i-1][j]:
            j -= 1
        else:
            i -= 1
res.reverse()
print(*res,sep='')

'''
AGTGATG
GTTAG

AATCC
ACACG

ABCBDAB
BDCABA
'''