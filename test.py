from heapq import heapify,heappush,heappop
li=[5,15,10,20,8,25,18]
k = 3
heap = []
heapify(heap)
for i in range(k):
    heappush(heap,li[i])

for i in range(k,len(li)):
    if heap[0] > li[i]:
        continue
    else:
        heappop(heap)
        heappush(heap,li[i])

print(heap)