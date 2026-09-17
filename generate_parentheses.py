# Tags: backtracking
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        path = ""
        
        def backtrack(use: int, have: int):
            nonlocal path
            if use == 0 and have == 0:
                result.append(path)
                return
            if use > 0:
                path += ')'
                backtrack(use-1, have)
                path = path[0:-1]
            if have > 0:
                path += '('
                backtrack(use + 1, have - 1)
                path = path[0:-1]
        
        
        backtrack(0, n)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(n = 3))
