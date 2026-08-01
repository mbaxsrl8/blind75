# Tags: intervals, sorting, greedy

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        res = 0
        intervals = sorted(intervals)
        prev_tail = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]>= prev_tail:
                prev_tail = interval[1]
            else:
                if prev_tail >= interval[1]:
                    prev_tail = interval[1]
                res += 1
        
        return res
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals = [[1,2],[2,4]]))
