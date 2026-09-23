# Tags: depth-first-search, graph, union-find

from typing import List

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree should have exact n-1 edges
        if len(edges) != n - 1:
            return False
        
        parents = list(range(n))
        size = [1 for _ in range(n)]
        
        def findRoot(node: int):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        for u, v in edges:
            root_u = findRoot(u)
            root_v = findRoot(v)
            
            if root_u == root_v:
                return False
            
            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u
            
            size[root_u] += size[root_v]
            parents[root_v] = root_u

        return True
    
if '__main__' == __name__:
    sol = Solution()
    print(sol.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
