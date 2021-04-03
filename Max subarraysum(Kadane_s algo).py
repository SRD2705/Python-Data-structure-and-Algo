# Kadane's Algorithm
# Find the maximum subarray sum
# Time: O(n)

def max_subarray_sum(li):
    n = len(li)
    max_so_far = 0
    max_ending = 0
    st = 0
    en = 0
    tmp = 0
    for i in range(n):
        max_ending += li[i]
        if max_so_far < max_ending:
            max_so_far = max_ending
            st = tmp
            en = i
        if max_ending < 0:
            max_ending = 0
            tmp += i
    print("The maximum subarray sum is: ", max_so_far)
    print("The maximum subarray sum start from index {} to index {}".format(st, en))


# It handle the case of all negetive numbers
def max_subarray_sum_neg(li):
    max_so_far = li[0]
    curr_max = li[0]
    n = len(li)

    for i in range(1, n):
        curr_max = max(li[i], curr_max + li[i])
        max_so_far = max(max_so_far, curr_max)

    print("The maximum subarray sum is: ", max_so_far)


li = list(map(int, input().split()))
max_subarray_sum(li)
max_subarray_sum_neg(li)

'''
Input: 
-2 -3 4 -1 -2 1 5 -3
Output:
The maximum subarray sum is:  7
The maximum subarray sum start from index 1 to index 6
'''
