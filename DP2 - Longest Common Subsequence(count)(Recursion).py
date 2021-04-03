################################ Longest Common Subsequence(count)(Recursion) ############################
'''
In this problem you are given two strings and you have to find out the longest common subsequence
base case:
If any of the array become zero then we return 0
condition:
if match:
we add 1 and call the function again with decrement both length by 1
if not match:
we can take max of two cases.
'''

li1 = list(input())
li2 = list(input())
n = len(li1)
m = len(li2)

def lcs(li1,li2,n,m):
    if n==0 or m==0:
        return 0
    if li1[n-1] == li2[m-1]:
        return 1+lcs(li1,li2,n-1,m-1)
    else:
        return max((lcs(li1,li2,n-1,m)),lcs(li1,li2,n,m-1))
print(lcs(li1,li2,n,m))
