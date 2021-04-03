'''
******[0-1 Knapsack(Recursive only)]******
For recursion we need a base case.The best approach of finding base case is
to think of the minimum possible valid input.In this case both are 0.

Now the next step is the decision diagram which means we include the itm in our
knapsack or not.

If the item weight is more than the knapsack weight then its not possible to take it.
So we ignore the item and check for the other items.
If the item weight is less then we will take the max value of
(the value after taking, and value without taking)
At last it gives us the max value.

'''


def knapsack(val,wt,w,n):
    if w == 0 or n == 0:
        return 0
    if wt[n-1] <= w:
        return max((val[n-1]+knapsack(val,wt,w-wt[n-1],n-1)),knapsack(val,wt,w,n-1)) # Getting the max valur
    else:
        return knapsack(val,wt,w,n-1)  # Check for other value



val = list(map(int, input().split()))
wt = list(map(int, input().split()))
w = int(input())
n = len(val)
print(knapsack(val,wt,w,n))
