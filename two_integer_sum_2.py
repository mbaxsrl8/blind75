# Tags: two-pointers

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                break
            elif sum > target:
                r -= 1
            else:
                l += 1
            
        
        return [l + 1, r + 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(numbers = [1,2,3,4], target = 3))
