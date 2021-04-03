# Longest common subsequence(LCS)
# Using Recursion only
# Time: O(2 ** n)

def lcs(A, B):
    if not A or not B:
        return ""
    x, m, y, n = A[0], A[1:], B[0], B[1:]
    if x == y:
        return x + lcs(m, n)
    else:
        return max(lcs(A, n), lcs(m, B), key=len)


print(lcs("thisisatest", "testingLCS123testing"))
