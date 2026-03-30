class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i -1]:
                operations += len(nums) - i
        return operations