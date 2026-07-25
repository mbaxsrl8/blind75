
# Tags: dfs, hash-map, graph

from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.map = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node.val not in self.map:
            mirror = Node(node.val)
            self.map[node.val] = mirror
        else:
            return self.map[node.val]
        for neighbor in node.neighbors:
            mirror.neighbors.append(self.cloneGraph(neighbor))
        
        return mirror
    
    
if '__main__' == __name__:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    sol = Solution()
    sol.cloneGraph(node1)
    
