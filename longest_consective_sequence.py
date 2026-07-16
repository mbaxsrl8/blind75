# Tags: hash-map
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cache = set()
        for num in nums:
            cache.add(num)
        res = 1
        for num in nums:
            if (num - 1) not in cache:
                continue

            i = 1
            while (num + i) in cache:
                i += 1
            res = max(res, i + 1)
        return res
        

if '__main__' == __name__:
    sol = Solution()
    print(sol.longestConsecutive(nums = []))