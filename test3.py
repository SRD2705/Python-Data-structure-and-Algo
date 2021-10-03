class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, cap):
        self.capacity = cap
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def add_to_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def set(self,key,val):
        if key in self.map:
            node = self.map[key]
            node.val = val
            self.delete(node)
            self.add_to_head(node)
        else:
            node = Node(key,val)
            self.map[key] = node
            if self.count < self.capacity:
                self.count += 1
                self.add_to_head(node)
            else:
                del self.map[self.tail.prev.key]
                self.delete(self.tail.prev)
                self.add_to_head(node)

    def get(self,key):
        if key in self.map:
            node = self.map[key]
            self.delete(node)
            self.add_to_head(node)
        else:
            return -1