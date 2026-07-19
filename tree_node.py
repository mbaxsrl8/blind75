from typing import List
from linked_list import ListNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        res = []
        level_nodes = [self]
        new_level = []
        while len(level_nodes) > 0:
            for node in level_nodes:
                res.append(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level_nodes = new_level
            new_level = []
        return str(res)
        
def convertListToTree(list: List) -> TreeNode:
    if len(list) == 0:
        return None
    root = TreeNode(list[0])
    level_nodes = [root]
    new_level = []
    i= 1
    while i < len(list):
        for node in level_nodes:
            node.left = TreeNode(list[i])
            i += 1
            new_level.append(node.left)
            if i == len(list):
                break
            node.right = TreeNode(list[i])
            i += 1
            if i == len(list):
                break
            new_level.append(node.right)
        level_nodes = new_level    
        new_level = []
    
    return root

def getNodeFromTree(root: TreeNode, val: int) -> TreeNode:
    if root is None:
        return None
    if root.val == val:
        return root
    left =  getNodeFromTree(root.left, val)
    if left:
        return left
    else:
        return getNodeFromTree(root.right, val)