# Tags: tree, design, bfs

from typing import Optional

from tree_node import TreeNode, convertListToTree


class Codec:
    def __init__(self):
        self.delimiter = '_'
        self.nullStr = 'N'

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        level = [root]
        new_level = []
        while len(level) > 0:
            for node in level:
                if node:
                    res.append(str(node.val))
                    new_level.append(node.left)
                    new_level.append(node.right)
                else:
                    res.append(self.nullStr)
            
            if all(
                node is None
                for node in new_level
            ):
                break
            level = new_level
            new_level = []
        return self.delimiter.join(res)
            

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = data.split(self.delimiter)
        if nodeList[0] == self.nullStr:
            return None
        root = TreeNode(int(nodeList[0]))
        level = [root]
        next_level = []
        i = 1
        while i < len(nodeList):
            for parent in level:
                parent.left = None if nodeList[i] == self.nullStr else TreeNode(int(nodeList[i]))
                i += 1
                parent.right = None if nodeList[i] == self.nullStr else TreeNode(int(nodeList[i]))
                i += 1
                if parent.left:
                    next_level.append(parent.left)
                if parent.right:
                    next_level.append(parent.right)
            level = next_level
            next_level = []
        
        
        return root


if __name__ == "__main__":
    codec = Codec()
    treeStr = codec.serialize(convertListToTree([1,2,3,None,None,4,5]))
    print(treeStr)
    root = codec.deserialize(treeStr)
    print(root)
