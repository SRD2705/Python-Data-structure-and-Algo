class stack:
    def __init__(self):
        self.arr = []
        self.min_st = []
        self.top = -1
        self.max = 100

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == self.max-1:
            return True
        return False

    def pop(self):
        if not self.is_empty():
            if self.min_st[-1] == self.arr[-1]:
                self.top -= 1
                self.min_st.pop()
                return self.arr.pop()
            else:
                self.top -= 1
                return self.arr.pop()
    def get_min(self):
        if self.top == -1:
            return -1
        return self.min_st[-1]


    def push(self,val):
        if not self.is_full():
            if self.is_empty():
                self.top += 1
                self.arr.append(val)
                self.min_st.append(val)
            else:
                self.top += 1
                self.arr.append(val)
                if self.min_st[-1] > val:
                    self.min_st.append(val)
            return

    def mini(self):
        if self.top == -1:
            return
        return self.arr[-1]

ob = stack()
ob.push(12)
ob.push(10)
ob.push(6)
ob.push(8)
ob.push(15)

print(ob.arr)
print(ob.min_st)
print(ob.get_min())
print(ob.pop())