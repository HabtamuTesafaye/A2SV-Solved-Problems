class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0,  len(height) - 1
        max_area = 0
        while left < right:
            # area = widht * height so width = right - left and height is the sorter wall from the left or right 
            area = (right - left ) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area