#Merge Sort
def merge(li):
    if len(li) > 1:
        m = len(li) // 2
        l = li[:m]
        r = li[m:]
        merge(l)
        merge(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                li[k] = l[i]
                i += 1
            else:
                li[k]= r[j]
                j += 1
            k += 1

        while i < len(l):
            li[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            li[k] = r[j]
            j += 1
            k += 1


li = list(map(int, input().split()))
merge(li)
print(*li)