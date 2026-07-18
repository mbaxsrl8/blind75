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
