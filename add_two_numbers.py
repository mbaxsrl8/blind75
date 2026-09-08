# Tags: linked-list
from typing import Optional

from linked_list import ListNode, convert_list_to_linked_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head1, head2 = l1, l2
        root = ListNode()
        dummy = ListNode(0)
        previous = root
        carry = 0
        while head1 or head2:
            if not head1:
                head1 = dummy
            if not head2:
                head2 = dummy
            val = head1.val + head2.val + carry
            carry = 0
            if val >= 10:
                carry = 1
                val -= 10
            cur = ListNode(val)
            previous.next = cur
            previous = cur
            head1, head2 = head1.next, head2.next
        
        if carry:
            previous.next = ListNode(1)

        return root.next


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.addTwoNumbers(
            convert_list_to_linked_list([9,9,9,9,9,9,9]),
            convert_list_to_linked_list([9,9,9,9]),
        )
    )
