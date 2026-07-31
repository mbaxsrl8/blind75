# Tags: two-pointers, string

# Given a string s, return the number of substrings within s that are palindromes.

# A palindrome is a string that reads the same forward and backward.

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def find_odd(i: int):
            nonlocal res
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        def find_even(i: int):
            nonlocal res
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            find_odd(i)
            find_even(i)

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("aaa"))
