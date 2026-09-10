# Tags: linked-list
from typing import Optional

from linked_list import ListNode, convert_list_to_linked_list


class Solution:
    
    @staticmethod
    def reverseList(head: ListNode, tail: ListNode):
        previous = None
        cur = head
        while cur != tail:
            nextCur = cur.next
            cur.next = previous
            previous = cur
            cur = nextCur
        tail.next = previous
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next:
            groupTail = cur.next
            groupCur = groupTail
            count = 1
            while groupCur.next and count < k:
                groupCur = groupCur.next
                count += 1
            if count < k:
                break
            groupHead = groupCur
            nextCur = groupHead.next
            self.reverseList(groupTail, groupHead)
            cur.next = groupHead
            groupTail.next = nextCur
            cur = groupTail
            
        
        return dummy.next
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseKGroup(convert_list_to_linked_list([1,2,3,4,5,6]), 3))
