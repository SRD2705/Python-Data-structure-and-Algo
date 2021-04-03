'''
******[0-1 Knapsack(Recursive + Memoization)]******
For recursion we need a base case.The best approach of finding base case is
to think of the minimum possible valid input.In this case both are 0.

In this case we make memoization matrix initialized with -1
when we get a specific value for n,w we update the value
In a recursion call if we found that m[w][n] then we don't need to run the recursion again
and return the value from the matrix



'''

m = [[-1 for j in range(1000)] for i in range(1000)]

def knapsack(val,wt,w,n):
    if w == 0 or n == 0:
        return 0
    if m[w][n] != -1:
        return m[w][n]
    if wt[n-1] <= w:
        m[w][n] = max((val[n-1]+ knapsack(val,wt,w-wt[n-1],n-1)),knapsack(val,wt,w,n-1))
        return m[w][n]
    elif wt[n-1] >= w:
        m[w][n] = knapsack(val,wt,w,n-1)
        return m[w][n]


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