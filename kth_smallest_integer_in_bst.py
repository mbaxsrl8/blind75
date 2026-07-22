# Tags: tree, stack
from typing import List, Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        i = 0
        while i < k:
            while cur:
                stack.append(cur)
                cur = cur.left
            if len(stack) > 0:
                cur = stack.pop()
                i += 1
                if i == k:
                    return cur.val
            cur = cur.right
                
        
        
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     list = self.convertBST2List(root)
    #     return list[k - 1]

    # def convertBST2List(self, root: TreeNode) -> Optional[List[int]]:
    #     if not root:
    #         return []
    #     return (
    #         self.convertBST2List(root.left)
    #         + [root.val]
    #         + self.convertBST2List(root.right)
    #     )


if "__main__" == __name__:
    sol = Solution()
    root = convertListToTree([4, 3, 5, 2, None])
    print(sol.kthSmallest(root, 4))
