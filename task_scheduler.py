# Tags: greedy, heap
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        result = 0
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
            
        while heap:
            task_executed = []
            while heap and len(task_executed) < n + 1:
                task_count = heapq.heappop(heap)
                task_executed.append(task_count)
            for count in task_executed:
                if -count > 1:
                    heapq.heappush(heap, count + 1)
            
            if not heap:
                result += len(task_executed)
            else:
                result += n + 1
            
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(tasks=["X","X","Y","Y"], n = 2))
