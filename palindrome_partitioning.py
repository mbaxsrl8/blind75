# Tags: backtracking, review-priority
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []
        
        def backtrack(start: int):
            if start == len(s):
                result.append(path.copy())
                return
            
            for end in range(start, len(s)):
                slice = s[start : end + 1]
                l, r = start, end
                valid = True
                while l < r:
                    if s[l] != s[r]:
                        valid = False
                        break
                    l += 1
                    r -= 1
                if valid:
                    path.append(slice)
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return result
                        
            


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition(s="bb"))
