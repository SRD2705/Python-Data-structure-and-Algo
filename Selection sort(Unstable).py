#Selection sort

li = list(map(int, input().split()))
n = len(li)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if li[min_idx] > li[j]:
            min_idx = j
    li[i], li[min_idx] = li[min_idx], li[i]
print(li)