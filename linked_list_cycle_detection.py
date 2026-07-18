# Tags: linked-list, two-pointers
from typing import Optional

from linked_list import ListNode, convert_list_to_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if slow is None:
            return False
        fast = head.next
        while fast and slow:
            if fast == slow:
                return True
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False       
        
        
if '__main__' == __name__:
    sol = Solution()
    start = convert_list_to_linked_list([1,2,3,4])
    tail = start
    while tail.next:
        tail = tail.next
    tail.next = start.next
    print(sol.hasCycle(start))
