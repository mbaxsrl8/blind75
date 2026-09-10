# Tags: heap
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, stone2 - stone1)
        return -heap[0] if heap else 0
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2,3,6,2,4]))
