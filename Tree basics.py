from queue import Queue

import zmq


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
        preorder(root.left, res)
        preorder(root.right, res)
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


def inorder_iter(root, res):
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


def postorder_iter(root, res):
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


def node_at_distance_k(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data, end=" ")
    else:
        node_at_distance_k(root.left, k - 1)
        node_at_distance_k(root.right, k - 1)


def height(root):
    if root:
        return max(height(root.left), height(root.right)) + 1
    else:
        return 0


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


def max_val(root):
    if root:
        return max(root.data, max(max_val(root.left), max_val(root.right)))
    else:
        return float("-inf")


def leftview(root, level, max_level):
    if root == None:
        return
    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level
    leftview(root.left, level + 1, max_level)
    leftview(root.right, level + 1, max_level)


def leftview_iter(root):
    if root:
        q = Queue()
        q.put(root)
        while not q.empty():
            count = q.qsize()
            for i in range(count):
                node = q.get()
                if i == 0:
                    print(node.data, end=" ")
                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)
    else:
        return


def rightview(root):
    if root is None:
        return []
    q = []
    res = []
    q.append(root)
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            node = q.pop(0)
            if i == count - 1:
                res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res


def topview(root):
    if root is None:
        return []
    d = {}
    q = []
    res = []
    q.append([root, 0])
    while len(q) > 0:
        tmp = q.pop(0)
        node = tmp[0]
        hd = tmp[1]
        if hd not in d.keys():
            d[hd] = node.data
        if node.left:
            q.append([node.left, hd - 1])
        if node.right:
            q.append([node.right, hd + 1])
    k = sorted(d.keys())
    for i in k:
        res.append(d[i])
    return res


def bottomview(root):
    if root is None:
        return []
    d = {}
    q = []
    res = []
    q.append([root, 0])
    while len(q) > 0:
        tmp = q.pop(0)
        node = tmp[0]
        hd = tmp[1]
        if hd not in d.keys():
            d[hd] = [node.data]
        else:
            d[hd].append(node.data)
        if node.left:
            q.append([node.left, hd - 1])
        if node.right:
            q.append([node.right, hd + 1])
    k = sorted(d.keys())
    for i in k:
        res.append(d[i][-1])
    return res


def check_children_sum(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    sum = 0
    if root.left is not None:
        sum += root.left.data
    if root.right is not None:
        sum += root.right.data

    return (root.data == sum and check_children_sum(root.left) and check_children_sum(root.right))


def check_for_balance(root):
    if root is None:
        return 0
    lh = check_for_balance(root.left)
    if lh == -1:
        return -1
    rh = check_for_balance(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1


def max_width(root):
    q = []
    res = 0
    q.append(root)
    while len(q) > 0:
        count = len(q)
        tmp = 0
        for i in range(count):
            node = q.pop(0)
            tmp += 1
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        res = max(res, tmp)
    return res


def tree_spiral(root):
    q = []
    res = []
    q.append(root)
    st = False
    while len(q) > 0:
        count = len(q)
        for i in range(count):
            node = q.pop(0)
            res.append(node.data)
            if st == False:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            else:
                if node.right is not None:
                    q.append(node.right)
                if node.left is not None:
                    q.append(node.left)
        if st == False:
            st = True
        else:
            st = False
        q.reverse()
    return res


def diameter_height(root, res):
    if root == None:
        return 0
    lh = diameter_height(root.left, res)
    rh = diameter_height(root.right, res)
    res[0] = max(res[0], 1 + lh + rh)
    return 1 + max(lh, rh)


def diameter_tree(root):
    # Code here
    res = [float('-inf')]
    k = diameter_height(root, res)
    return res[0]


def lca(root, n1, n2):
    # Code here
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    lca1 = lca(root.left, n1, n2)
    lca2 = lca(root.right, n1, n2)
    if lca1 != None and lca2 != None:
        return root
    if lca1 != None:
        return lca1
    else:
        return lca2


if __name__ == '__main__':
    root = bintree(1)
    root.left = bintree(2)
    root.right = bintree(3)
    root.left.left = bintree(4)
    root.left.right = bintree(5)
    root.right.left = bintree(6)
    root.right.right = bintree(7)
    # print("The height of the tree is: ", height(root))
    # li_pre = []
    # li_in = []
    # li_post = []
    # li_bfs = []
    # print(preorder(root, li_pre))
    # print(preorder_iter(root, li_pre))
    # print(inorder(root, li_in))
    # print(inorder_iter(root, li_in))
    # print(postorder(root, li_post))
    # print(postorder_iter(root, li_post))
    # print(bfs(root, li_bfs))
    # node_at_distance_k(root, 2)
    # print()
    # print(max_val(root))
    # max_level = [0]
    # leftview(root, 1, max_level)
    # print()
    # leftview_iter(root)
    # print()
    # print(check_children_sum(root))
    # print(check_for_balance(root))
    # print(max_width(root))
    # print(tree_spiral(root))
    # print(diameter_tree(root))
    # print(lca(root,4,5).data)
    print(rightview(root))
    print(topview(root))
    print(bottomview(root))
