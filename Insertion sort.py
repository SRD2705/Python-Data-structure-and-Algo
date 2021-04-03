#Insertion Sort

li = list(map(int, input().split()))
n = len(li)
for i in range(1, n):
    tmp = li[i]
    j = i - 1
    while j >= 0 and tmp < li[j]:
        li[j+1] = li[j]
        j -= 1
    li[j+1] = tmp
print(li)