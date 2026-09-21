# Tags: breadth-first-search, matrix
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        round = 0
        rows, cols = len(grid), len(grid[0])
        
        queue = deque(
            (r, c, 0)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c] == 2
        )
        
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, cur = queue.popleft()
            round = cur
            for move in next_moves:
                nr = r + move[0]
                nc = c + move[1]
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, cur + 1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:        
                    return -1
        return round
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting(grid = [[1,1,0],[0,1,1],[0,1,2]]))
