################################ Longest Common Subsequence(Count)(Recursion+Memoization) ######################
'''
In this case we just use a memoization which is nothing just a matrix
we initialize the matrix with -1 and update the value.
The reason of memoization is if we already calculate a function with same parameter
then we dont need to calculate because it is store in the table.
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)
t = [[-1 for i in range(m+1)] for j in range(n+1)]

def lcs(li1,li2,n,m,t):
    if n==0 or m==0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    else:
        if li1[n-1] == li2[m-1]:
            t[n][m] = 1 + lcs(li1,li2,n-1,m-1,t)
            return t[n][m]
        else:
            t[n][m] = max((lcs(li1,li2,n,m-1,t)),lcs(li1,li2,n-1,m,t))
            return t[n][m]
print(lcs(li1,li2,n,m,t))