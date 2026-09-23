# Tags: breadth-first-search, graph, union-find
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1 for _ in range(n)]
        res = n
        
        def findRoot(node: int):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        for u, v in edges:
            root_u = findRoot(u)
            root_v = findRoot(v)
            
            if root_u == root_v:
                continue
            
            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u
            
            size[root_u] += size[root_v]
            parent[root_v] = root_u
            res -= 1
            
        return res
        
                
if '__main__' == __name__:
    sol = Solution()
    print(sol.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))
