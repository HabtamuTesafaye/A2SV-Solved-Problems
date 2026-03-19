class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reiminders = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            reiminder =  prefix_sum % k 

            if reiminder in reiminders:
                if i - reiminders[reiminder] >= 2:
                    return True
            else:
                reiminders[reiminder] = i
        
        return False