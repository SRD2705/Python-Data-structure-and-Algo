# KMP algorithm
# to fing a patttern in a substring we use this algo
#Time = O(m+n) Space = O(m)

def table(pat):
    m = len(pat)
    li = [0] * m #the final table initialize with zero
    k = 0
    for i in range(1, m):
        while k>0 and pat[i] != pat[k]:
            k = li[k-1]
        if pat[i] == pat[k]:
            k += 1
        li[i] = k
    return li

def kmp(txt,pat):
    n = len(txt)
    m = len(pat)
    li = table(pat)
    q = 0
    for i in range(n):
        while q>0 and txt[i] != pat[q]:
            q = li[q-1]
        if txt[i] == pat[q]:
            q += 1
        if q == m:      #end condition that we found the string
            return i - m + 1
    return 1

print(kmp("abcdfdcab", "ab"))
