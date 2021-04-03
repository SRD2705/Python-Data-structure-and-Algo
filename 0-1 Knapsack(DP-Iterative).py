'''
******[0-1 Knapsack(DP-Iterative)]******
For recursion we need a base case.The best approach of finding base case is
to think of the minimum possible valid input.In this case both are 0.

In this program we do not use recursion and we use DP

'''

def knapsack(val,wt,w,n):
    m = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                m[i][j] = 0
            elif wt[i-1] <= j:
                m[i][j] = max((val[i-1] + m[i-1][j-wt[i-1]]), m[i-1][j])
            else:
                m[i][j] = m[i-1][j]
    return m[n][w]


val = list(map(int, input().split()))
wt = list(map(int, input().split()))
w = int(input())
n = len(val)
print(knapsack(val,wt,w,n))
'''
60 100 120
10 20 30
50
'''