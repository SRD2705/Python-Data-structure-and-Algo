from heapq import heappop,heappush,heapify

def mergek(li,k):
    heap = []
    for i in range(k):
        heappush(heap, [li[i][0],[i,0]])
    # print(heap)
    res = []
    while heap:
        tmp = heappop(heap)
        res.append(tmp[0])
        if tmp[1][1] + 1 < n:
            heappush(heap,[li[tmp[1][0]][tmp[1][1]+1],[tmp[1][0],tmp[1][1]+1]])
    return res

n = int(input())
k = int(input())
li = []
for i in range(k):
    tmp = list(map(int, input().split()))
    li.append(tmp)
print(mergek(li,k))


'''
3
3
2 4 6
0 1 9
3 4 5
'''