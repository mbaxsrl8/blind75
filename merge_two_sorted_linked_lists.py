# Tags: linked-list
from typing import Optional

from linked_list import *

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        start = head
        
        while list1 and list2:
            new_head = None
            if list1.val > list2.val:
                new_head = list2
                list2 = list2.next
            else:
                new_head = list1
                list1 = list1.next
            head.next = new_head
            head = new_head
        
        if list1:
            head.next = list1
        if list2:
            head.next = list2
            
        return start.next
        
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.mergeTwoLists(convert_list_to_linked_list([]), convert_list_to_linked_list([1,3,5])))
