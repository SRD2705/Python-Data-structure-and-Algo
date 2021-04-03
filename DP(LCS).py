# Largest common Subsequence
# Using DP
# Time O(mn)
# Space O(mn)

def lcs(A, B):
    table = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i, x in enumerate(A):
        for j, y in enumerate(B):                        # Enumerate will also track the iteration number and return
            if x == y:                                   # an enumerate object
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    result = ""
    x, y = len(A), len(B)
    while x != 0 and y != 0:
        if table[x][y] == table[x - 1][y]:
            x -= 1
        elif table[x][y] == table[x][y - 1]:
            y -= 1
        else:
            assert A[x - 1] == B[y - 1]  # If it became false then assert will return an assertion error
            result = A[x - 1] + result
            x -= 1
            y -= 1
    return result


print(lcs('thisisatest', 'testingLCS123testing'))
