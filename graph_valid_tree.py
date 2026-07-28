# Tags: dfs, graph

from typing import List

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cache = [[] for _ in range(n)]
        for edge in edges:
            cache[edge[0]].append(edge[1])
            cache[edge[1]].append(edge[0])
        
        status = [0 for _ in range(n)] # 0: unvisited  1: visiting 2: visited
        
        def dfs_hasCircle(node: int, parent: int) -> bool:
            if status[node] == 2:
                return False
            elif status[node] == 1:
                return True
            status[node] = 1
            for child in cache[node]:
                if child == parent:
                    continue
                if dfs_hasCircle(child, node):
                    return True
            status[node] = 2
            return False
            
        if dfs_hasCircle(0, -1):
            return False
        
        return all(
            status[i] == 2
            for i in range(1, n)
        )
    
if '__main__' == __name__:
    sol = Solution()
    print(sol.validTree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
