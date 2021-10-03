########################### Count number of subsets with a given difference #######################################
'''
In this problem you are given an array and a d(difference)
we have to count number of subset of the difference d
so s1 + s2 = sum(array)
   s1 - s2 = d
  --------------
  2s1 = sum(array) + d
  s1 = (sum(array) + d) // 2
so if we found subsets of sum s1 then the difference is possible otherwise not
now if sum(array)+d is odd then no subset possible
else:
so we need to count the subset of sum s1 which is basically count subset sum problem.
we go to the subproblem( Count subset sum)
we pass the array and s1 as the parameter and gives the answer
'''

def count_subset_sum(li,k):
    n = len(li)
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for j in range(n + 1):
        dp[j][0] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            if j >= li[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-li[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][k]
li = list(map(int, input().split()))
d = int(input())
s = sum(li)
if (d+s) % 2 != 0:
    print(0)
else:
    k = (d+s) // 2
    res = count_subset_sum(li,k)
    print(res)
