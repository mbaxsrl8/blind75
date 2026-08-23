# Tags: tree, recursion
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:   
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            return q is None
        if not q:
            return p is None
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     level_nodes = [root]
    #     new_level = []
    #     while len(level_nodes) > 0:
    #         for node in level_nodes:
    #             if not node:
    #                 continue
    #             if self.isSameTree(node, subRoot):
    #                 return True
    #             new_level.append(node.left)
    #             new_level.append(node.right)
    #         level_nodes = new_level
    #         new_level = []
    #     return False
            
    
    
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p:
    #         return q is None
    #     if not q:
    #         return p is None
    #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if '__main__' == __name__:
    sol = Solution()
    root = convertListToTree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
    subRoot = convertListToTree([1,None,1,None,1,None,1,None,1,None,1,2])
    print(sol.isSubtree(root, subRoot))
