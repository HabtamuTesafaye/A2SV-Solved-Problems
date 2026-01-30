from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        frequency = Counter(nums)
        majority = []

        for num, count in frequency.items():
            if count > n // 3:
                majority.append(num)
        return majority
