# Tags: sliding-window, sliding-window
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            while not self.isalpha(s[l]) and l < r:
                l += 1
            while not self.isalpha(s[r]) and l < r:
                r -= 1
            if l == r:
                return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isalpha(self, c: str):
        return ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")

    # def isPalindrome(self, s: str) -> bool:
    #     new_str = ''
    #     for c in s:
    #         if c.isalnum():
    #             new_str += c.lower()
    #     return new_str == new_str[::-1]


if "__main__" == __name__:
    sol = Solution()
    print(sol.isPalindrome(s=",."))
