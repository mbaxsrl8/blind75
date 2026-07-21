# Tags: tree, breadth-first-search
from typing import List, Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level_nodes = [root]
        new_level = []
        while len(level_nodes) > 0:
            res_new = []
            for node in level_nodes:
                if not node:
                    continue
                res_new.append(node.val)
                new_level.append(node.left)
                new_level.append(node.right)
            if len(res_new) > 0:
                res.append(res_new)
            level_nodes = new_level
            new_level = []
        return res
    

if '__main__' == __name__:
    sol = Solution()
    root = convertListToTree([1,2,3,4,5,6,7])
    print(sol.levelOrder(root))
