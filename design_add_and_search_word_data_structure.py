# Tags: design, string, trie, hash-map, depth-first-search

class TrieNode:

    def __init__(self, val=None, isLeaf=False):
        self.children = {}
        self.val = val
        self.isLeaf = isLeaf


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                node = TrieNode(c)
                cur.children[c] = node
            cur = cur.children[c]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int):
            if i == len(word):
                return node.isLeaf
            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
            else:
                return any(
                   dfs(next, i + 1) 
                   for next in node.children.values()
                )

        return dfs(self.root, 0)


if "__main__" == __name__:
    wd = WordDictionary()
    wd.addWord("a")
    wd.addWord("abcdefghijklmnopqrst")
    print(wd.search("a"))
    print(wd.search("abcdefghijklmnopqrst"))
