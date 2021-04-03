################################################################ Palindrome Partition(Recursion) ######################################################################################
'''
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome.
For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.
Determine the fewest cuts needed for a palindrome partitioning of a given string.
For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”.
If a string is a palindrome, then minimum 0 cuts are needed.
If a string of length n containing all different characters, then minimum n-1 cuts are needed.
'''

import sys
def ispalin(s):
    return s == s[::-1]

def pal_part(s,i,j):
    if i >= j or ispalin(s[i:j+1]):
        return 0
    res = sys.maxsize
    for k in range(i,j):
        tmp = 1 + pal_part(s,i,k) + pal_part(s,k+1,j)
        res = min(tmp,res)
    return res

li = list(input())
print(pal_part(li,0,len(li)-1))