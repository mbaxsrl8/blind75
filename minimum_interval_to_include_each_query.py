# Tags: intervals, greedy, heap
import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals = sorted(intervals)
        sortedQueries = sorted(queries)
        answers: dict[int, int] = {}
        
        heap = []
        i = 0
        for index, query in enumerate(sortedQueries):
            if index -1 >= 0 and query == sortedQueries[index-1]:
                continue
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            answers[query] = heap[0][0] if heap else -1

        return [answers[query] for query in queries]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minInterval(intervals=[[2,3],[2,5],[1,8],[20,25]], queries=[2,19,5,22]))