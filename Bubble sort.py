#bubble sort
li = list(map(int,input().split()))
n = len(li)
for i in range(n):
    for j in range(1, n):
        if li[j] < li[j-1]:
            li[j], li[j-1] = li[j-1], li[j]
print(li)