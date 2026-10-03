# Tags: heap, matrix, greedy, needs-review
import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        N = len(grid)
        
        nextMoves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while ((N-1, N-1) not in visited):
            maxH, r, c = heapq.heappop(minHeap)
            if (r, c) not in visited:
                visited.add((r, c))
            else:
                continue
            if r == N-1 and c == N-1:
                return maxH
            for nextMove in nextMoves:
                nr = r + nextMove[0]
                nc = c + nextMove[1]
                if 0<=nr<N and 0<=nc<N and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(maxH, grid[nr][nc]), nr, nc))


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.swimInWater(
            grid=[[0, 1, 2, 10], 
                  [9, 14, 4, 13], 
                  [12, 3, 8, 15], 
                  [11, 5, 7, 6]]
        )
    )
