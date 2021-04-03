#Stock price(maximumprofit)
#Time: O(n)
#space:O(1)

n = int(input())
li = list(map(int, input().split()))
cost = 0
max_cost = 0
if n == 0:
    print(0)
min_price = li[0]
for i in range(n):
    min_price = min(min_price, li[i])
    cost = li[i] - min_price
    max_cost = max(max_cost, cost)
print("Buy at {0}th day".format(li.index(min_price)))
print("Sell at {}th day ".format(li.index(min_price+max_cost)))
print("Maximum profit: ", max_cost)

'''
Input: 100 180 260 310 40 535 695
Output: 
Buy at 4th day
Sell at 6th day 
Maximum profit:  655
'''