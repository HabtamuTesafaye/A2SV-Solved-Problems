class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        total_sum = sum(nums)
        return actual_sum - total_sum
