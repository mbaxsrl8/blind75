# Tags: linked-list, hash-map
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        old_to_new = {}
        cur = head
        tail = dummy
        while cur:
            tail.next = Node(cur.val)
            old_to_new[cur] = tail.next
            cur = cur.next
            tail =  tail.next
        
        for original,copy in old_to_new.items():
            if original.random:
                copy.random = old_to_new[original.random]
        
        return dummy.next
            
    

if __name__ == "__main__":
    node3 = Node(3)
    node7 = Node(7)
    node4 = Node(4)
    node5 = Node(5)
    node3.next = node7
    node7.next = node4
    node7.random = node5
    node4.next = node5
    node4.random = node3
    node5.random = node7
    print(Solution().copyRandomList(node3))
