class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        running_sum = 0
        for num in nums:
            running_sum += num
            result.append(running_sum)

        return result