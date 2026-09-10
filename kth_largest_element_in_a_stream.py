# Tags: design, heap
from typing import List
import heapq
# from collections import deque


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     nums = sorted(nums, reverse=True)
    #     if len(nums) >= k:
    #         self.stack = deque(nums[:k])
    #     else:
    #         self.stack = deque(nums)
        

    # def add(self, val: int) -> int:
    #     poped = []
    #     if not self.stack:
    #         self.stack.append(val)
    #     elif val >= self.stack[0]:
    #         self.stack.appendleft(val)
    #     else:
    #         while self.stack and val > self.stack[-1]:
    #             poped.append(self.stack.pop())
    #         self.stack.append(val)
    #     while len(self.stack) < self.k:
    #         self.stack.append(poped.pop())
    #     while len(self.stack) > self.k:
    #         self.stack.pop()
    #     return self.stack[-1]
    
if __name__ == "__main__":
    container = KthLargest(3, [1, 2, 3, 3])
    print(container.add(3))
    print(container.add(5))
    print(container.add(6))
    print(container.add(7))
    print(container.add(8))
