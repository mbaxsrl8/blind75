# Tags: tree
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def getLeftAndRightDiameter(head: TreeNode) -> tuple[int, int]:
            nonlocal result
            leftDiameter, rightDiameter = 0, 0
            if head.left:
                leftDiameter = max(getLeftAndRightDiameter(head.left)) + 1
            if head.right:
                rightDiameter = max(getLeftAndRightDiameter(head.right)) + 1
            result = max(result, leftDiameter + rightDiameter)
            return (leftDiameter, rightDiameter)
        
        getLeftAndRightDiameter(root)
        return result
        
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.diameterOfBinaryTree(convertListToTree([1,None,2,3,4,5])))
