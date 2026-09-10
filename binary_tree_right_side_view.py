# Tags: tree, breadth-first-search
from typing import List, Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        level_nodes = [root]
        next_level = []
        while level_nodes:
            result.append(level_nodes[-1].val)
            for node in level_nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level_nodes = next_level
            next_level = []       
        
        return result
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.rightSideView(convertListToTree([1,2,3,None,4,None,5])))
