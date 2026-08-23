# Tags: intervals, review-priority

from typing import List
# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        new_head = newInterval[0]
        if i < len(intervals) and intervals[i][0] < new_head:
            new_head = intervals[i][0]

        while i < len(intervals) and intervals[i][1] <= newInterval[1]:
            i += 1
        new_tail = newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            new_tail = intervals[i][1]
            i += 1
        res.append([new_head, new_tail])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
    

if '__main__' == __name__:
    sol = Solution()
    print(sol.insert(intervals = [[1,5]], newInterval = [2,3]))
