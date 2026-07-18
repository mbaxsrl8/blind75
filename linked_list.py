from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = str(self.val)
        next = self.next
        if next is not None:
            res += '-->' + str(next)
        return res

def convert_list_to_linked_list(list: List) -> ListNode:
    return build_list_node(0, list)
        
def build_list_node(index: int, list: List) -> ListNode:
    if index >= len(list):
        return None
    head = ListNode(list[index])
    head.next = build_list_node(index + 1, list)
    return head