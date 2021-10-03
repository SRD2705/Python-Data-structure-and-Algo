# Max heap implementation

class MinHeap:
    def __init__(self, cap):
        self.heap = [0] * cap
        self.cap = cap
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return (2 * index) + 1

    def get_right_child_index(self, index):
        return (2 * index) + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def parent(self, index):
        return self.heap[self.get_parent_index(index)]

    def left_child(self, index):
        return self.heap[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heap[self.get_right_child_index(index)]

    def is_full(self):
        return self.size == self.cap

    def is_empty(self):
        return self.size == 0

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapifyup(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) < self.heap[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapifydown(self):
        index = 0
        while self.has_left_child(index):
            small = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                small = self.get_right_child_index(index)
            if self.heap[index] < self.heap[small]:
                self.swap(index, small)
            else:
                break
            index = small

    def push(self, data):
        if self.is_full():
            print("Heap is Full")
            return
        self.heap[self.size] = data
        self.size += 1
        self.heapifyup()
        print(self.heap)

    def pop(self):
        if self.is_empty():
            print("Empty Heap")
            return
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifydown()
        return data

if __name__ == '__main__':
    heap = MinHeap(10)
    heap.push(12)
    heap.push(11)
    heap.push(9)
    heap.push(0)
    heap.push(85)
    heap.push(33)
    heap.push(52)
    heap.push(1)
    print(heap.heap)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.heap)