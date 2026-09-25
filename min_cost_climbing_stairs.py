class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        previous2, previous1 = 0, 0
        for i in range(2, len(cost) + 1):
            minCost = min(previous2 + cost[i - 2], previous1 + cost[i - 1])
            previous2, previous1 = previous1, minCost
        return previous1