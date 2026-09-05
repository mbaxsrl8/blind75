# Tags: stack, monotonic-queue
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        widths = [1] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                previous = stack.pop()
                widths[i] += widths[previous]
                widths[previous] += i - previous - 1
                
            stack.append(i)
        
        for i in stack:
            widths[i] += stack[-1] - i

        max_area = 0
        for i, width in enumerate(widths):
            max_area = max(max_area, width * heights[i])
        return max_area
    
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea(heights = [3,6,5,7,4,8,1,0]))
