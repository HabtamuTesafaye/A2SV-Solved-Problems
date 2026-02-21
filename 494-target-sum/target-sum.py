class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        subset_target = (total_sum + target) // 2
        
        # dp[i] will store the number of ways to reach sum i
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # One way to reach sum 0 (empty subset)
        
        for num in nums:
            # Iterate backwards to avoid using the same element multiple times 
            # in the same iteration (standard 0/1 knapsack optimization)
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]