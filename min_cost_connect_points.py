# Tags: graph, minimum-spanning-tree, needs-review
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Prim's Algo
        minHeap = [(0, 0)]
        visited = set()
        result = 0
        while len(visited) <= len(points) - 1:
            cost, v1 = heapq.heappop(minHeap)
            if v1 in visited:
                continue
            visited.add(v1)
            result += cost
            x1, y1 = points[v1][0], points[v1][1]
            for i in range(len(points)):
                if i == v1 or i in visited:
                    continue
                x2, y2 = points[i][0], points[i][1]
                distance = abs(x1- x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (distance, i))
        return result
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
