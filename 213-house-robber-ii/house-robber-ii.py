class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_line(nums[:-1]), self.rob_line(nums[1:]))

    def rob_line(self, nums):
        prev1 = 0
        prev2 = 0
        
        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp
        
        return prev1