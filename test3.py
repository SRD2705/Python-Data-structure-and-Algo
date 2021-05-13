def ispal(li):
    if li == reversed(li):
        return True
    else:
        return False
print(ispal('aacaa'))