def fibnum(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibnum(n-1) + fibnum(n-2)

allfib = [0,1]


def findfib(n):
    if n in allfib:
        return allfib[n]
    else:
        for i in range(len(allfib), n+1):
            lst = allfib[-1]
            seclst = allfib[-2]
            allfib.append(lst+seclst)
        return allfib[n]


for i in range(int(input())):
    n = int(input())
    print(findfib(n))