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

n,w = map(int, input().split())
val = [1]*(n)
wt = list(map(int, input().split()))
print(knapsack(val,wt,w,n))