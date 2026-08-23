# Tags: backtracking, dfs, matrix, string
from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        next_move = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r: int, c:int, visited: Set, i: int) -> bool:
            if i == len(word):
                return True
            
            visited.add((r,c))
            for move in next_move:
                nr = r + move[0]
                nc = c + move[1]
                if (nr >=0 and nr < len(board) 
                    and nc >=0 and nc < len(board[0]) 
                    and (nr, nc) not in visited 
                    and board[nr][nc] == word[i]):
                    if dfs(nr,nc,visited,i+1):
                        return True
            visited.remove((r,c))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    if dfs(row, col, set(), 1):
                        return True
        
        return False


if "__main__" == __name__:
    sol = Solution()
    print(
        sol.exist(
            board=[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
            word="ABCESEEEFS",
        )
    )
