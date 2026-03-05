class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right = 0,len(nums) - 1
        operations = 0

        while left < right:
            corrent_sum = nums[left] + nums[right]
            if corrent_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif corrent_sum < k:
                left += 1
            else:
                right -= 1

        return operations
