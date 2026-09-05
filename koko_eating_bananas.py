# Tags: binary-search
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        if h < len(piles):
            return -1
        l,r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            if time > h:
                l = m + 1
            else:
                r = m
        return l

if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed(piles=[3,6,7,11], h=8))
