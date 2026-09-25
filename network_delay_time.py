# Tags: heap, graph, breadth-first-search, needs-review
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edgeMap = {}
        for s, d, t in times:
            if s not in edgeMap:
                edgeMap[s] = []
            edgeMap[s].append([d, t])
        
        level = [(0, k)]
        next_level = []
        visited = set()
        timeElapsed = 0
        while level:
            minTime = level[0][0]
            timeElapsed += minTime
            for time, node in level:
                if time != minTime:
                    heapq.heappush(next_level, (time - minTime, node))
                    continue
                if node in visited:
                    continue
                else:
                    visited.add(node)
                    if len(visited) == n:
                        return timeElapsed
                if node not in edgeMap:
                    continue
                for neighbor, timeToReach in edgeMap[node]:
                    heapq.heappush(next_level, (timeToReach, neighbor))
            level = next_level
            next_level = [] 
        
        return -1
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1))
