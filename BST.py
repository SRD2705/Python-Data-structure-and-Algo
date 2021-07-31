class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if root.data > key:
        return search(root.left, key)
    else:
        return search(root.right, key)


def find_next(curr):
    curr = curr.right
    while curr != None and curr.left != None:
        curr = curr.left
    return curr


def delnode(root, key):
    if root == None:
        return root
    if root.data > key:
        root.left = delnode(root.left, key)
    elif root.data < key:
        root.right = delnode(root.right, key)
    else:
        if root.left is None:
            tmp = Node(root.right)
            root = None
            return tmp
        elif root.right is None:
            tmp = Node(root.left)
            root = None
            return tmp
        else:
            tmp = find_next(root)
            root.data = tmp.data
            root.right = delnode(root.right, tmp.data)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def floor(root, key):  # O(h),O(1)
    res = None
    while root is not None:
        if key == root.data:
            return root
        elif key < root.data:
            root = root.left
        else:
            res = root
            root = root.right
    return res


def ceil(root, key):  # O(h),O(1)
    res = None
    while root is not None:
        if root.data == key:
            return root
        elif root.data > key:
            res = root
            root = root.left
        else:
            root = root.right
    return res.data


# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    r = delnode(r, 40)

    # Print inoder traversal of the BST
    inorder(r)
    print()
    print(search(r, 50))
    print(floor(r, 20))
    print(ceil(r, 25))
