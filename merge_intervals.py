# Tags: intervals, sorting

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        head = intervals[0][0]
        tail = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= tail:
                tail = max(intervals[i][1], tail)
            else:
                res.append([head, tail])
                head = intervals[i][0]
                tail = intervals[i][1]
        res.append([head, tail])
        
        return res
    
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.merge(intervals = [[1,3],[1,5],[6,7]]))
