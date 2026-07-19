# Tags: linked-list, two-pointers
from typing import Optional

from linked_list import ListNode, convert_list_to_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = l
        i = 0
        while i < n:
            r = r.next
            i += 1
        while r.next:
            l = l.next
            r = r.next

        next_node = l.next.next
        l.next.next = None
        l.next = next_node 
        return dummy.next
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     end = self.reverseList(head)
    #     dummy = ListNode(0, end)
    #     p = dummy
    #     i = 0
    #     while i < n - 1:
    #         p = p.next
    #         i = i + 1
        
    #     next_node = p.next.next
    #     p.next.next = None
    #     p.next = next_node
        
    #     return self.reverseList(dummy.next)

        
        
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            next_head = head.next
            head.next = tail
            tail = head
            head = next_head
        return tail
        
        
if '__main__' == __name__:
    sol = Solution()
    head= convert_list_to_linked_list([5])
    print(sol.removeNthFromEnd(head, 1))
