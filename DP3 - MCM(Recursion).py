#################################### MCM(Recursion) ##########################
'''
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
https://media.geeksforgeeks.org/wp-content/uploads/matrixchainmultiplication.png
https://www.youtube.com/watch?v=kMK148J9qEE&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=34

'''

import sys
def mcm(li,i,j):
    if i >= j:
        return 0
    res = sys.maxsize
    for k in range(i,j):
        tmp = mcm(li,i,k)+mcm(li,k+1,j)+(li[i-1] * li[k] * li[j])
        res = min(res,tmp)
    return res


li = list(map(int, input().split()))
n = len(li)
res = mcm(li,1,n-1)
print(res)
'''
40 20 30 10 30
10 20 30 40 30
'''