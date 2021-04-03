#problem of train/bus platform needed
#time: O(nlogn)
#space: O(1)

lia = list(map(int, input().split()))
lid = list(map(int, input().split()))
lia.sort() #sort according to time
lid.sort()
n = len(lia)
res = 1 #actual platform needed
tmp = 1 #tmp varible to calculate the platform
i = 1
j = 0
while (i < n and j < n):
    if lia[i] <= lid[j]:
        tmp += 1
        i += 1
    elif lia[i] > lid[j]:
        tmp -= 1
        j += 1
    if tmp > res:
        res = tmp
print(res)

'''''
Input stream:
900 940 950 1100 1500 1800
910 1200 1120 1130 1900 2000

output:
3
'''''
