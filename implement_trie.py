# Tags: hash-map, string, design
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {} # key is val. v is TreeNode
        self.isLeaf = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children.keys():
                cur.children[c] = TreeNode(c)
            cur = cur.children.get(c)
        cur.isLeaf = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children.keys():
                return False
            cur = cur.children.get(c)
        return cur.isLeaf

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children.keys():
                return False
            cur = cur.children.get(c)
        return True


if "__main__" == __name__:
    trie = PrefixTree()
    trie.insert("dog")
    print(trie.search("dog"))
    print(trie.search("do"))
    print(trie.startsWith("do"))
    trie.insert("do")
    print(trie.search("do"))
