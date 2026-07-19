# Tags: tree, recursion
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left_tree= root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left_tree)
        return root
        
        
if '__main__' == __name__:
    sol = Solution()
    root = convertListToTree([1,2,3,4,5,6,7])
    print(sol.invertTree(root))
