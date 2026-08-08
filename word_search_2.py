# Tags: backtracking, trie, matrix, dfs

class TrieNode:
    def __init__(self):
        self.childern = {}
        self.words = set()
        self.index = 0
        

class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = []
        
        for word in words:
            i = 0
            parent = self.root
            while i < len(word):
                c = word[i]
                if c not in parent.childern:
                    parent.childern[c] = TrieNode()
                parent = parent.childern[c]
                parent.index = parent.index + 1
                i+=1 
            parent.words.add(word)

        rows = len(board)
        cols = len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def dfs(r: int, c: int, node: TrieNode) -> int:
            dfs_res = 0
            original = board[r][c]
            board[r][c] = None

            if node.words:
                for word in node.words:
                    res.append(word)
                dfs_res = len(node.words)
                node.words = None

            prune = set()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    0<=nr<rows
                    and 0<=nc<cols
                    and board[nr][nc]
                ):
                    char = board[nr][nc]
                    child = node.childern.get(char)
                    if child and child.index != 0:
                        dfs_res += dfs(nr, nc, node.childern[char])
                        if child.index == 0:
                            prune.add(char)
            for p in prune:
                del node.childern[p]
            board[r][c] = original
            node.index -= dfs_res
            return dfs_res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in self.root.childern:
                    node = self.root.childern[board[i][j]]
                    if node.index != 0:
                        dfs(i, j, node)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.findWords(
            board=[["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]],
            words=["bat","cat","back","backend","stack", "abas", "dkac"]
        )
    )
