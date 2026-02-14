class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Sort each row to make the largest on the right side
        for row in nums:
            row.sort()
        
        score = 0
        cols = len(nums[0])
        
        # For each column, take the maximum among all rows
        for j in range(cols):
            best = 0
            for i in range(len(nums)):
                best = max(best, nums[i][j])
            score += best
        
        return score
