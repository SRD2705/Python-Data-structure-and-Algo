li = list(map(int, input().split()))
res = 0
st = 0
tmp = 0
for i in range(len(li)):
    if li[i] % 2 == 0:
        if st == False or st == 0:
            tmp += 1
            st = True
            res = max(res, tmp)
        else:
            tmp = 1
            st = True
    else:
        if st == True or st == 0:
            st = False
            tmp += 1
            res = max(res,tmp)
        else:
            tmp = 1
            st = False
print(res)