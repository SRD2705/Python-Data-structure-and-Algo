class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,key):
        ptr = self.root
        for i in key:
            ind = ord(i)-ord('a')
            if ptr.children[ind] == None:
                ptr.children[ind] = TrieNode()
            ptr = ptr.children[ind]
        ptr.is_end = True
    def search(self,key):
        ptr = self.root
        for i in key:
            ind = ord(i)-ord('a')
            if ptr.children[ind] == None:
                return False
            ptr = ptr.children[ind]
        if ptr != None and ptr.is_end == True:
            return True
        else:
            return False

t = Trie()
t.insert("tree")
t.insert("is")
t.insert("our")
t.insert("ourself")
t.insert("truth")

print(t.search("ou"))