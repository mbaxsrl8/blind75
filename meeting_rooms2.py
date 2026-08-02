# Tags: two-pointers, greedy, sorting, heap

import heapq


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # use 2 pointer
        start_time = sorted([i.start for i in intervals])
        end_time = sorted([i.end for i in intervals])

        s, e = 0, 0
        while s < len(intervals):
            if start_time[s] >= end_time[e]:
                e += 1
            s += 1
        return s - e

    # def minMeetingRooms(self, intervals: list[Interval]) -> int:
    #     # use min heap
    #     intervals.sort(key=lambda interval: (interval.start, interval.end))
    #     ending_time = []
    #     for interval in intervals:
    #         if len(ending_time) == 0:
    #             ending_time.append(interval.end)
    #         else:
    #             earliest_endingTime = heapq.heappop(ending_time)
    #             if interval.start < earliest_endingTime:
    #                 heapq.heappush(ending_time, earliest_endingTime)
    #             heapq.heappush(ending_time, interval.end)

    #     return len(ending_time)

    # def minMeetingRooms(self, intervals: list[Interval]) -> int:
    #     # O(n^2)
    #     if len(intervals) == 0:
    #         return 0
    #     res = 0

    #     def arrange(meetings: list[Interval]):
    #         nonlocal res
    #         res += 1
    #         if len(meetings) == 1:
    #             return
    #         unarranged = []
    #         prev_meeting = meetings[0]
    #         for i in range(1, len(meetings)):
    #             if meetings[i].start < prev_meeting.end: # have conflict
    #                     unarranged.append(meetings[i])
    #             else:
    #                prev_meeting = meetings[i]
    #         if len(unarranged) > 0:
    #             arrange(unarranged)

    #     arrange(intervals)
    #     return res


if __name__ == "__main__":
    sol = Solution()
    intervalTupleList = [(1, 5), (5, 10), (10, 15), (15, 20), (1, 20), (2, 6)]
    print(sol.minMeetingRooms([Interval(s[0], s[1]) for s in intervalTupleList]))
