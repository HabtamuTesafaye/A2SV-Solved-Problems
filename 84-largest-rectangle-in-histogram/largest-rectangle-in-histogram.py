class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        stack.append(0)
        heights.append(0)
        
        for i ,val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                local_height = heights[stack.pop()]
                width = 0
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_area = max(max_area, local_height * width)
            stack.append(i)
        return max_area
            