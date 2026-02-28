class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        max_product = nums[-2] * nums[-1]
        min_product = nums[1] * nums[0]

        return max_product - min_product