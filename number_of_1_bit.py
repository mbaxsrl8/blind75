class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     res = 0
    #     while n:
    #         res += n % 2
    #         n = n >> 1
    #     return res

    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res


if "__main__" == __name__:
    sol = Solution()
    print(sol.hammingWeight(0o01111111111111111111111111111101))
