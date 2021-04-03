import sys, threading

def main1():
    n, m = map(int, input().split())
    cost = list(map(int, input().split()))
    pairs = {}

    def addValueToDict(key, value):
        if key in pairs:
            pairs[key].append(value)
        else:
            l = list()
            l.append(value)
            pairs[key] = l

    for i in range(m):
        line3 = input().split(' ')
        key = int(line3[0]) - 1
        value = int(line3[1]) - 1

        addValueToDict(key, value)
        addValueToDict(value, key)

    # print(pairs)

    trackArr = [0] * n

    def minCost(key):
        costVal = 0

        if trackArr[key] == 0:
            trackArr[key] = 1
            costVal = cost[key]

            if key in pairs:
                for val in pairs[key]:
                    if trackArr[val] == 0:
                        childCost = minCost(val)
                        if childCost < costVal:
                            costVal = childCost

        return costVal

    totalCost = 0

    for i in range(n):
        if trackArr[i] == 0:
            totalCost += minCost(i)

    print(totalCost)

# Recursion and thread optimization if recusrion limit reach
if __name__ == "__main__":
    sys.setrecursionlimit(9100000)

    threading.stack_size(134217728)

    main_thread = threading.Thread(target=main1)
    main_thread.start()
    main_thread.join()

