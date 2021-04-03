######################################### Longest reapeating subsequence(count+print) #############################################
'''
in this problem you are given a string and you need to find the string which is most repeated
NOTE: We can use one letter for one subsequence only,no repetition
So approach is we take li2 as  the same string so if we do lcs we get the same length of the original string
because both are the same string.
we just make one check that if we found two letter same and we increase the count if i != j
we put that condition because we can not use the same element in two subsequence so if
same letter found in another position then it can be counted otherwise not.
'''

li1 = list(input())
li2 = li1
n = len(li1)
m = len(li2)
dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if li1[i-1] == li2[j-1] and i != j:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[n][m])

i = n
j = m
res = []
while i > 0 and j > 0:
    if li1[i-1] == li2[j-1] and i != j:
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
