# Tags: tree, recursion
from typing import Optional

from tree_node import TreeNode, convertListToTree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return q is None
        if not q:
            return p is None
        return p.val == q. val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     level_p = [p]
    #     level_q = [q]
    #     new_level_p = []
    #     new_level_q = []
    #     while len(level_p) > 0 and len(level_q) > 0:
    #         for i in range(0, len(level_p)):
    #             if level_p[i] is None or level_q[i] is None:
    #                 if level_p[i] != level_q[i]:
    #                     return False
    #                 else:
    #                     continue
    #             if level_p[i].val != level_q[i].val:
    #                 return False
    #             if level_p[i]:
    #                 new_level_p.append(level_p[i].left)
    #                 new_level_p.append(level_p[i].right)
    #             if level_q[i]:
    #                 new_level_q.append(level_q[i].left)
    #                 new_level_q.append(level_q[i].right)
    #         level_p = new_level_p
    #         new_level_p = []
    #         level_q = new_level_q
    #         new_level_q = []
    #     return len(level_p) == len(level_q)
    

if '__main__' == __name__:
    sol = Solution()
    print(sol.isSameTree(convertListToTree([1,2,3]), convertListToTree([1,2,3])))
