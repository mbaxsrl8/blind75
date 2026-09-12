# Tags: tree, depth-first-search
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(head: TreeNode) -> int:
            if not head:
                return 0
            left = getHeight(head.left)
            if left == -1:
                return -1
            right = getHeight(head.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return getHeight(root) != -1
    

if __name__ == "__main__":
    sol =Solution()
    print(sol.isBalanced(convertListToTree([3,9,20,None,None,15,7])))
