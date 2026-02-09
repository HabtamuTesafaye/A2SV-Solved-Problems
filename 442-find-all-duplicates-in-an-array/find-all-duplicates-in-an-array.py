class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicate = []

        for i in range(1, len(nums)):
            # sicne we  soryed the number same number likly appear together compare them 
            if nums[i] == nums[i - 1]:
                duplicate.append(nums[i])
        return duplicate