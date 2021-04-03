from queue import Queue


class bintree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setdata(self, data):
        self.data = data

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right


def preorder(root, res):
    if root:
        res.append(root.data)
        preorder(root.left,res)
        preorder(root.right,res)
    return res


def preorder_iter(root, res):
    s = []
    if root:
        s.append(root)
        while s:
            node = s.pop()
            res.append(node.data)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
    return res


def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.data)
        inorder(root.right, res)
    return res


def inorder_iter(root,res):
    if root:
        s = []
        node = root
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                res.append(node.data)
                node = node.right
    return res


def postorder(root, res):
    if root:
        postorder(root.left, res)
        postorder(root.right, res)
        res.append(root.data)
    return res


def postorder_iter(root,res):
    if root:
        vis = set()
        s = []
        node = root
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if node.right and node.right not in vis:
                    s.append(node)
                    node = node.right
                else:
                    vis.add(node)
                    res.append(node.data)
                    node = None
    return res


def bfs(root, res):
    q = Queue()
    q.put(root)
    node = None
    while not q.empty():
        node = q.get()
        res.append(node.getdata())
        if node.getleft() is not None:
            q.put(node.getleft())
        if node.getright() is not None:
            q.put(node.getright())
    return res


if __name__ == '__main__':
    root = bintree(1)
    root.left = bintree(2)
    root.right = bintree(3)
    root.left.left = bintree(4)
    root.left.right = bintree(5)
    root.right.left = bintree(6)
    root.right.right = bintree(7)
    li_pre = []
    li_in = []
    li_post = []
    li_bfs = []
    print(preorder(root, li_pre))
    print(preorder_iter(root,li_pre))
    print(inorder(root, li_in))
    print(inorder_iter(root,li_in))
    print(postorder(root, li_post))
    print(postorder_iter(root, li_post))
    print(bfs(root, li_bfs))