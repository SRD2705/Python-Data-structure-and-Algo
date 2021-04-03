    ###################### Equal sum partition(T or F) #####################
'''
So basically you given an array and you have to find out that,
two partition of the array with equal sum possible or not
Firstly, if the sum of the array is odd then return false because
it is not possible to divide equally(because of integer value)

else:
do the same as subset sum problem.
The slight change is that you have to find (sum // 2).If you make it then other part must be (sum//2)

'''
li = list(map(int, input().split()))
s = sum(li)
n = len(li)

if s%2 != 0:
    print("False")
else:
    s = s//2
    d = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(s+1):
        d[0][i] = False
    for i in range(n + 1):
        d[i][0] = True
    # print(d)
    for i in range(1,n+1):
        for j in range(1,s+1):
            d[i][j] = d[i-1][j]
            if j >= li[i-1]:
                d[i][j] = (d[i-1][j-li[i-1]]) or (d[i-1][j])
    print(d[n][s])