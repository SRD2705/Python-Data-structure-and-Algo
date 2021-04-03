def partition(li, low, high):
    i = (low - 1)  
    pivot = li[high] 

    for j in range(low, high):
        if li[j] < pivot:
            i = i + 1
            li[i], li[j] = li[j], li[i]

    li[i + 1], li[high] = li[high], li[i + 1]
    return (i + 1)

def quickSort(li, low, high):
    if low < high:
        pi = partition(li, low, high)
        quickSort(li, low, pi - 1)
        quickSort(li, pi + 1, high)


li = list(map(int, input().split()))
n = len(li)
quickSort(li, 0, n - 1)
print(li)