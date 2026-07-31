# Tags: dp, string

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current += prev1
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                current += prev2
            prev2 = prev1
            prev1 = current

        return current


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("1012"))
