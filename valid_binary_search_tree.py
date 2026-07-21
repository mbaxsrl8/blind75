# Tags: tree, binary-search-tree
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTWithVal(root, -1001, 1001)

    
    def isValidBSTWithVal(self, root: Optional[TreeNode], min: int, max: int) -> bool:
        if not root:
            return True
        res = (root.val > min) & (root.val < max)
        left_tree = root.left
        right_tree = root.right
        if left_tree:
            res &= self.isValidBSTWithVal(left_tree, min, root.val)
        if right_tree:
            res &= self.isValidBSTWithVal(right_tree, root.val, max)
        return res

if "__main__" == __name__:
    sol = Solution()
    root = convertListToTree([5, 4, 6, None, None, 3, 7])
    print(sol.isValidBST(root))
