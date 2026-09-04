# Tags: stack, monotonic-queue, review-priority
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        widths = [0] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                previous = stack.pop()
                widths[i] += widths[previous] + 1
                widths[previous] += i-previous
                
            stack.append(i)
        for i in stack:
            widths[i] += stack[-1] - i + 1
        
        max_area = 0
        for i , width in enumerate(widths):
            max_area = max(max_area, width * heights[i])

        return max_area
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea(heights = [7,1,7,2,2,4]))
