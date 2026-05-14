class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)

        if len(nums) != mx + 1:
            return False

        count = Counter(nums)

        for i in range(1, mx):
            if count[i] != 1:
                return False

        return count[mx] == 2