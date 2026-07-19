# Tags: linked-list, two-pointers
from typing import Optional

from linked_list import ListNode, convert_list_to_linked_list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        start = head
        while start:
            n += 1
            start = start.next

        if n < 3:
            return
        head2_index = n // 2 + 1
        i = 0
        head2 = head
        while i < head2_index - 1:
            i += 1
            head2 = head2.next
        # breakdown list
        end_list1 = head2
        head2 = end_list1.next
        end_list1.next = None

        head2 = self.reverse_list(head2)
        while head and head2:
            next_head = head.next
            next_head2 = head2.next
            head.next = head2
            head2.next = next_head
            head = next_head
            head2 = next_head2

    def reverse_list(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            next = head.next
            head.next = tail
            tail = head
            head = next
        return tail


if "__main__" == __name__:
    sol = Solution()
    head = convert_list_to_linked_list([2, 4, 6, 8, 10])
    sol.reorderList(head)
    print(head)
