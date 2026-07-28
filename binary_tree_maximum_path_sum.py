# Tags: tree, dp

from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    
    def __init__(self):
        self.res = -1000
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def sumUp(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = sumUp(node.left)
            right = sumUp(node.right)
            subRes = max(max(left, right) + node.val, node.val)
            self.res = max(self.res, subRes, left + right + node.val)
            return subRes
            
        
        sumUp(root)
        return self.res           


if "__main__" == __name__:
    sol = Solution()
    print(sol.maxPathSum(convertListToTree([-15,10,20,None,None,15,5,-5])))
