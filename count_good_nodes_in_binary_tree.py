# Tags: tree
from tree_node import TreeNode, convertListToTree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(head: TreeNode, prevMax: int) -> int:
            if not head:
                return 0
            result = dfs(head.left, max(prevMax, head.val)) + dfs(head.right, max(prevMax, head.val))
            if head.val >= prevMax:
                result += 1
            return result
        return dfs(root, -101)
            
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.goodNodes(convertListToTree([2,1,1,3,None,1,5])))
