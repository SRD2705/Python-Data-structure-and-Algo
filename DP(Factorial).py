# DP Factorial

d = {}
def fact(n):
    if n == 0:
        d[0] = 1
        return 1
    else:
        d[n] = n*fact(n-1)
        return d[n]
print(fact(3))