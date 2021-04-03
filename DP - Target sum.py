################# Target Sum ##########################
'''
In this problem we are given an array and a sum
We can assign + or - and how many subset give the sum
so this problem may look horrible but it is same as Count subset of given difference
because,
take the example 1 1 2 3 and the target sum is 1
one,
+1+1+3-3 = 1
so subsets are,
s1 = +1 +1 +2
s2 = -3
two,
-1+1-2+3
so subsets are,
s1 = -1 -2
s2 = +1 +3
three,
+1-1-2+3
so the subsets are,
s1 = +1 +3
s2 = -1 -2

so all case what we do is making two subsets and and get the difference of their sum

'''
def count_subset_sum(li,s):
    n = len(li)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(s+1):
        dp[0][i] = False
    for j in range(n+1):
        dp[j][0] = True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if j >= li[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-li[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]

li = list(map(int, input().split()))
d = int(input())
k = sum(li)
res = 0
if (k+d) % 2 != 0:
    print(0)
else:
    s = (k+d) // 2
    res = count_subset_sum(li,s)
    print(res)