# Tags: tree, recursion, divide-and-conquer
"""Construct Binary Tree from Preorder and Inorder Traversal."""

from typing import List, Optional

from tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])

        i = 0
        while inorder[i] != root.val:
            i += 1
        root.left = self.buildTree(preorder[1 : i + 1], inorder[0:i])
        root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])

        return root


if "__main__" == __name__:
    sol = Solution()
    print(sol.buildTree(preorder=[1, 2, 3, 4], inorder=[2, 1, 3, 4]))
