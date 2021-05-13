from itertools import product
n = int(input())
mod=1000000000+7
x = int(input())
d = int(input())
li = list(range(1,n+1,1))
tmp = []
res = 0
for i in product(1,repeat=2):
    if li[0]^li[1] <= x and (li[0]+li[i])%d == 0:
        res += 1

print(res%mod)
