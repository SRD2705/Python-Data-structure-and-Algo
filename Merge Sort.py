n, k = map(int, input().split())
li = list(map(int, input()))
tmp = [0]
res = 0
for i in range(n):
    if abs(li[i]-k) in tmp:
        res += 1
    else:
        tmp.append(abs(li[i]-k))
print(res)