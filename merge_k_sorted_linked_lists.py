# Tags: linked-list, heap
from typing import List, Optional
import heapq
import itertools

from linked_list import ListNode, convert_list_to_linked_list


class Solution:    
    def mergeSort(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # do not use heap
        if not lists or len(lists) == 0:
            return None
        merged_list = []
        
        while len(lists) > 1:
            for i in range(0, len(lists), 2):
                l2 = None
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                merged_list.append(self.merge2sortedList(lists[i], l2))
            lists = merged_list 
            merged_list = []
        
        return lists[0]
        
        
    def merge2sortedList(self, l1:Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        
        return dummy.next
    
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use min heap
        counter = itertools.count()
        pointers = []
        for node in lists:
            head = node
            while head:
                heapq.heappush(pointers, (head.val, next(counter), head))
                head = head.next
        if len(pointers) == 0:
            return None
        head = heapq.heappop(pointers)[2]
        node = head
        while len(pointers) > 0:
            node.next = heapq.heappop(pointers)[2]
            node = node.next
        
        
        return head
        
        

if '__main__' == __name__:
    sol = Solution()
    lists = [convert_list_to_linked_list(list) for list in [[1,2,4],[1,3,5],[3,6]]]
    print(sol.mergeSort(lists))
