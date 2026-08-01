# Tags: intervals, sorting

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings(intervals = [Interval(5,8),Interval(9,15)]))
