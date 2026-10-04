# Tags: greedy
class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        def validA(a, b, c) -> bool:
            return a == target[0] and b <= target[1] and c <= target[2]

        def validB(a, b, c) -> bool:
            return a <= target[0] and b == target[1] and c <= target[2]

        def validC(a, b, c) -> bool:
            return a <= target[0] and b <= target[1] and c == target[2]

        resultA, resultB, resultC = False, False, False

        for a, b, c in triplets:
            resultA |= validA(a, b, c)
            resultB |= validB(a, b, c)
            resultC |= validC(a, b, c)

        return resultA and resultB and resultC


if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeTriplets(triplets=[[1, 2, 3], [7, 1, 1]], target=[7, 2, 3]))
