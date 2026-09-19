# Tags: backtracking
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates = sorted(candidates)
        result = []
        path = []
        
        def backtrack(start: int, remaining: int):
            if remaining == 0:
                result.append(path.copy())
                return
            
            for i in range(start, len(candidates)):
                if i - 1 >= start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()
        
        backtrack(0, target)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2(candidates = [9,2,2,4,6,1,5], target = 8))
