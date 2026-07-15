# Tags: hash-map, sorting
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(0, len(nums))]
        cache = dict()
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        for num, count in cache.items():
            bucket[count - 1].append(num)
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) != 0:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        break
                if len(res) == k:
                        break
        return res
            
        
        
if '__main__' == __name__:
    sol = Solution()
    print(sol.topKFrequent(nums = [1,2,2,3,3,3], k = 2))