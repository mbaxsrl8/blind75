# Tags: linked-list, recursion
from typing import Optional

from linked_list import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterate
        hook = None
        while head is not None:
            next = head.next
            head.next = hook
            hook = head
            
            head = next
        return hook
    
    def recursivelyReverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        new_head = self.recursivelyReverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
        
if '__main__' == __name__:
    sol = Solution()
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    # sol.recursivelyReverse(node0).next = None
    
    print(sol.recursivelyReverse(node0))
