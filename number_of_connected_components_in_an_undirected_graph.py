from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        cache = [[] for _ in range(n)]
        for edge in edges:
            cache[edge[0]].append(edge[1])
            cache[edge[1]].append(edge[0])
            
        status = [0 for _ in range(n)] # 0: unvisited  1: visited
        for i in range(n):
            if status[i] == 0:
                res += 1
            else:
                continue
            bfs = [i]
            next_bfs = []
            while len(bfs) > 0:
                for j in bfs:
                    if status[j] != 0:
                        continue
                    status[j] = 1
                    neighbors = cache[j]
                    for neighbor in neighbors:
                        next_bfs.append(neighbor)
                bfs = next_bfs
                next_bfs = []
        
        return res
    
if '__main__' == __name__:
    sol = Solution()
    print(sol.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))
# Tags: bfs, graph
