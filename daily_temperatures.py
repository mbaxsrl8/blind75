# Tags: stack, monotonic-queue, review-priority
from collections import deque

# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = deque()
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous = stack.pop()
                res[previous] = i - previous
            stack.append(i)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures(temperatures=[89,62,70,58,47,47,46,76,100,70]))
