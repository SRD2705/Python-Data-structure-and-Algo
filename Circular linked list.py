class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class clinkedlist:
	def __init__(self):
		self.head = None

	def ins_end(self, data):
		if self.head is None:
			self.head = Node(data)
			self.head.next = self.head
			return
		tmp = self.head
		while tmp.next != self.head:
			tmp = tmp.next
		node = Node(data)
		tmp.next = node
		node.next = self.head

	def ins_beg(self, data):
		if self.head is None:
			self.head = Node(data)
			self.head.next = self.head
			return
		tmp = self.head
		while tmp.next != self.head:
			tmp = tmp.next
		node = Node(data)
		node.next = self.head
		tmp.next = node
		self.head = node

	def del_end(self):
		if self.head is None:
			print("Linked list is empty")
			return
		tmp = self.head
		var = tmp
		while tmp.next != self.head:
			var = tmp
			tmp = tmp.next
		var.next = self.head

	def del_beg(self):
		if self.head is None:
			print("Linke list is empty")
			return
		tmp = self.head
		while tmp.next != self.head:
			tmp = tmp.next
		tmp.next = self.head.next
		self.head = self.head.next


	def length(self):
		if self.head is None:
			return 0
		c = 1
		tmp = self.head
		while tmp.next != self.head:
			c += 1
			tmp = tmp.next
		return c

	def print(self):
		if self.head is None:
			print("Linked list is empty")
			return
		res = ''
		tmp = self.head
		while tmp:
			res += str(tmp.data) + '-->'
			tmp = tmp.next
			if tmp == self.head:
				break
		print(res)

if __name__ == '__main__':
	li = clinkedlist()
	li.ins_end(1)
	li.ins_end(2)
	li.ins_end(3)
	li.ins_beg(15)
	print(li.length())
	li.print()
	li.del_end()
	li.del_beg()
	li.print()
