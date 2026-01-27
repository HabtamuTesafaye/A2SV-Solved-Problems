from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)

        for num, count in frequency.items():
            if count > len(nums) // 2:
                return num
