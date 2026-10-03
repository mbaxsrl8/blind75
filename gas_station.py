# Tags: greedy, needs-review


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # if sum is >= cost, there must be a result
        total = 0
        start = 0
        for i in range(len(gas)):
            surplus = gas[i] - cost[i]
            total += surplus
            if total < 0:
                start = i + 1
        return start


if __name__ == "__main__":
    sol = Solution()
    print(sol.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))
