from typing import List

# Tags: bfs, matrix


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def isValidPos(pos: tuple[int, int])->bool:
            return pos[0] >=0 and pos[0] < len(grid) and pos[1] >=0 and pos[1] < len(grid[pos[0]])
        
        def bfs(posList: List[tuple[int, int]]) :
            neighbors = []
            for pos in posList:
                row, col = pos[0], pos[1]
                if pos in visited or grid[row][col] == "0":
                    continue
                visited.add(pos)
                if isValidPos((row - 1, col)) and (row - 1, col) not in visited and grid[row-1][col] == '1':
                    neighbors.append((row - 1, col))
                if isValidPos((row + 1, col)) and (row + 1, col) not in visited and grid[row+1][col] == '1':
                    neighbors.append((row + 1, col))
                if isValidPos((row, col - 1)) and (row, col - 1) not in visited and grid[row][col-1] == '1':
                    neighbors.append((row, col - 1))
                if isValidPos((row, col + 1)) and (row, col + 1) not in visited and grid[row][col+1] == '1':
                    neighbors.append((row, col + 1))
            
            if len(neighbors) > 0:    
                bfs(neighbors)
                
                
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs([(i, j)])
                    islands += 1
        return islands
                
    

if '__main__' == __name__:
    sol = Solution()
    print(sol.numIslands([
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]))
