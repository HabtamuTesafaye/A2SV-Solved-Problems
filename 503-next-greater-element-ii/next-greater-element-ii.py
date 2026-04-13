class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # stores indices

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                prev = stack.pop()
                result[prev] = nums[i % n]
            
            # Only push indices from the first pass
            if i < n:
                stack.append(i)

        return result