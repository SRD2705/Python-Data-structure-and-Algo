###################### COUNT OF SUBSET SUM OF A GIVEN SUM ##################################
'''
It is similer to subset sum(T or F) problem
Here you have to find how many subset are present
Initialise the dp table
just replace or with plus in the loop

'''

li = list(map(int, input().split()))
n = len(li)
s = int(input())
d = [[0 for i in range(s + 1)] for j in range(n + 1)]

for i in range(s + 1):
    d[0][i] = 0
for j in range(n + 1):
    d[j][0] = 1
# print(d)
for i in range(1, n + 1):
    for j in range(1, s + 1):
        d[i][j] = d[i - 1][j]
        if j >= li[i - 1]:
            d[i][j] = d[i - 1][j - li[i - 1]] + d[i][j]
print(d[n][s])
