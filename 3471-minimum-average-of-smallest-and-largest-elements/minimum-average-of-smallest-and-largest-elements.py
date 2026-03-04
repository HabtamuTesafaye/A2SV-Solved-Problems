class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        
        left = 0
        right = n - 1
        min_avg = float('inf')
        
        while left < right:
            avg = (nums[left] + nums[right]) / 2
            min_avg = min(min_avg, avg)
            left += 1
            right -= 1
        
        return min_avg