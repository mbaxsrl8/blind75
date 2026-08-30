# Tags: heap, sliding-window, monotonic-queue, review-priority

# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        window = deque()
        for index, value in enumerate(nums):
            # pop out left-most value
            if len(window) > 0 and window[0] <= index - k:
                window.popleft()
            while len(window) > 0 and nums[window[-1]] < value:
                window.pop()
            window.append(index)
            if index >= k -1:
                result.append(nums[window[0]])
        
        return result
        
    # def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    #     res = []
    #     window = []
    #     for i in range(k):
    #         heapq.heappush(window, -nums[i])
    #     res.append(-window[0])
    #     to_remove = []
    #     for i in range(k, len(nums)):
    #         heapq.heappush(window, -nums[i])
    #         if nums[i-k] == -window[0]:
    #             heapq.heappop(window)
    #             while len(to_remove) > 0 and to_remove[0] == window[0]:
    #                 heapq.heappop(to_remove)
    #                 heapq.heappop(window)
    #         else:
    #             heapq.heappush(to_remove, -nums[i-k])
    #         res.append(-window[0])
    #     return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [9,10,9,-7,-4,-8,2,-6], k = 5))
