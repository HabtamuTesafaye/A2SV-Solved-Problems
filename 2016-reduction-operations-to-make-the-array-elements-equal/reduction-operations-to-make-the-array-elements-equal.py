class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total_ops = 0
        for i in range(len(nums) - 1 , 0, -1):
            if nums[i] != nums[i -1]:
                total_ops += len(nums) - i

        return total_ops