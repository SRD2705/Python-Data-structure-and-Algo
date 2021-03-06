class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def ins_val(self,li):
        self.head = None
        for i in li:
            self.ins_end(i)

    def lngth(self):
        res = 0
        tmp = self.head
        while tmp:
            res += 1
            tmp = tmp.next
        return res
    def remove_at(self, i):
        if i < 0 or i >= self.lngth():
            raise Exception("Not a valid index")
        if i == 0:
            self.head = self.head.next
            return
        c = 0
        tmp = self.head
        while tmp:
            if c == i-1:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
            c += 1

    def get_ptr_node(self,k):
        tmp = self.head
        cnt = 0
        while tmp:
            if cnt == k-1:
                return tmp
            else:
                cnt += 1
                tmp = tmp.next



    def ins_bng(self, data):
        node = Node(data, self.head)
        self.head = node

    def ins_at(self,i,data):
        if i < 0 or i >= self.lngth():
            raise Exception("Not a valid Index")
        if i == 0:
            self.ins_bng(data)
            return
        c = 0
        tmp = self.head
        while tmp:
            if c == i - 1:
                node = Node(data, tmp.next)
                tmp.next = node
                break
            tmp = tmp.next
            c += 1

    def ins_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(data, None)

    def ins_aft_val(self, data_after, data):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data,self.head.next)
            return
        c = 0
        tmp = self.head
        while tmp:
            if tmp.data == data_after:
                tmp.next = Node(data, tmp.next)
                break
            tmp = tmp.next
            c += 1

    def remove_by_val(self,data):
        if self.head is None:
            return
        if self.head == data:
            self.head = self.head.next
            return
        c = 0
        tmp = self.head
        while tmp:
            if tmp.next.data == data:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

    def reverse(self):
        if self.head is None:
            print("linked list is empty")
            return
        last = None
        tmp = self.head
        while tmp:
            next_node = tmp.next
            tmp.next = last
            last = tmp
            tmp = next_node
        self.head = last

    def reverse_first_k_node(self,k):
        if self.lngth() < k or k < 0 or self.head is None:
            print("Not Possible")
            return
        else:
            last = self.get_ptr_node(k)
            # last = None
            first = self.head
            tmp = self.head
            cnt = 0
            while cnt != k+1:
                next_node = tmp.next
                tmp.next = last
                last = tmp
                tmp = next_node
                cnt += 1
            first.next = tmp
            self.head = last



    def print(self):
        if self.head is None:
            print("List is empty: ")
            return
        tmp = self.head
        strg = ''
        while tmp:
            strg += str(tmp.data) + ' --> '
            tmp = tmp.next
        print(strg)

if __name__ == '__main__':
    li = Linkedlist()
    li.ins_val([12,23,45,11,13,5])
    # li.remove_by_val(23)
    li.reverse_first_k_node(3)
    li.print()


