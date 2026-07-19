# Tags: tree, binary-search-tree
from tree_node import TreeNode, convertListToTree, getNodeFromTree


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

        return None
    
    def isSubTree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        return self.isSameTree(root, subRoot) or self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            return q is None
        if not q:
            return p is None
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if "__main__" == __name__:
    sol = Solution()
    root = convertListToTree([5, 3, 8, 1, 4, 7, 9, None, 2])
    p = getNodeFromTree(root, 3)
    q= getNodeFromTree(root, 4)
    print(sol.lowestCommonAncestor(root, p, q).val)
    
