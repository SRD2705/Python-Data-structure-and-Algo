n = int(input("Enter a number: "))


def sqrt_number(n):
    high = n
    low = 1
    res = 0
    while high >= low:
        mid = (high + low) // 2
        if mid * mid > n:
            high = mid - 1
        elif mid * mid < n:
            low = mid + 1
            res = mid
        elif mid * mid == n:
            return mid

    return res

print(sqrt_number(n))