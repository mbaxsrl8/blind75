# Tags: dfs, matrix, review-priority

from typing import List, Set

# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Constraints:

# 1 <= heights.length, heights[r].length <= 100
# 0 <= heights[r][c] <= 1000


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols = len(heights[0])
        cache = [[[0,0] for i in range(cols)] for j in range(rows)]
        res = []
     
        next_moves = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r:int, c:int, pa: int):
            if cache[r][c][pa] == 1:
                return
            cache[r][c][pa] = 1
            for move in next_moves:
                nr = r + move[0]
                nc = c + move[1]
                if (nr >=0 and nr < rows and nc >=0 and nc < cols 
                    and cache[nr][nc][pa] == 0
                    and heights[nr][nc] >= heights[r][c]):
                    dfs(nr,nc,pa)

        for col in range(cols):
            dfs(0,col,0)
            dfs(rows-1,col,1)
        for row in range(rows):
            dfs(row,0,0)
            dfs(row,cols-1,-1)
        
        for row in range(rows):
            for col in range(cols):
                if cache[row][col][0] == 1 and cache[row][col][1] == 1:
                    res.append([row, col])


        return res
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     pac = set()
    #     atl = set()
        
    #     def getNextPostList(r: int, c: int, visited: Set[tuple[int, int]]) -> List[tuple[int, int]]:
    #         neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    #         res = []
            
    #         for n in neighbors:
    #             if (
    #                 n[0] >= 0
    #                 and (n[0] < len(heights))
    #                 and (n[1] >= 0)
    #                 and (n[1] < len(heights[n[0]]))
    #                 and (n not in visited)
    #                 and (heights[r][c] <= heights[n[0]][n[1]])
    #             ):
    #                 res.append(n)
    #         return res
        
    #     def dfs(r: int, c: int, visited: Set[tuple[int, int]]):
    #         visited.add((r, c))
    #         neighbors = getNextPostList(r, c, visited)
    #         for n in neighbors:
    #             dfs(n[0], n[1], visited)
                
                
    #     for col in range(0, len(heights[0])):
    #         dfs(0, col, pac)
    #         dfs(len(heights) - 1, col, atl)
                    
    #     for row in range(0, len(heights)):
    #         dfs(row, 0, pac)
    #         dfs(row, len(heights[row]) - 1, atl)
            
            
    #     res = []
    #     for co in pac:
    #         if co in atl:
    #             res.append([co[0], co[1]])
        
    #     return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.pacificAtlantic(heights=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
