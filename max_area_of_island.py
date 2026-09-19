# Tags: depth-first-search, matrix
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        next_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r: int, c: int) -> int:
            res = 1
            visited.add((r, c))
            for move in next_moves:
                nr = r + move[0]
                nc = c + move[1]
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                    res += dfs(nr, nc)
            return res
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    result = max(result, dfs(r, c))
        
        return result
            


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.maxAreaOfIsland(
            grid=[[0, 1, 1, 0, 1], 
                  [1, 0, 1, 0, 1], 
                  [0, 1, 1, 0, 1], 
                  [0, 1, 0, 0, 1]]
        )
    )
