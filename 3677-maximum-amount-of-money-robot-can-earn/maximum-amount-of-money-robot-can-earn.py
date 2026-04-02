class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
    
        # dp[i][j][k] = max coins at (i,j) with k neutralizations used
        # k can be 0, 1, or 2
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case: starting position
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            # At start, we can either take the penalty or neutralize
            dp[0][0][0] = coins[0][0]  # take penalty
            dp[0][0][1] = 0  # neutralize
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):  # k neutralizations used so far
                    # Try coming from top (i-1, j)
                    if i > 0:
                        for prev_k in range(k + 1):
                            if dp[i-1][j][prev_k] == -float('inf'):
                                continue
                            
                            if coins[i][j] >= 0:
                                # Positive cell: just add coins
                                if prev_k == k:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i-1][j][prev_k] + coins[i][j])
                            else:
                                # Negative cell: take penalty or neutralize
                                # Option 1: take penalty
                                if prev_k == k:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i-1][j][prev_k] + coins[i][j])
                                # Option 2: neutralize (if we have budget)
                                if prev_k + 1 == k and k <= 2:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i-1][j][prev_k])
                    
                    # Try coming from left (i, j-1)
                    if j > 0:
                        for prev_k in range(k + 1):
                            if dp[i][j-1][prev_k] == -float('inf'):
                                continue
                            
                            if coins[i][j] >= 0:
                                # Positive cell: just add coins
                                if prev_k == k:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i][j-1][prev_k] + coins[i][j])
                            else:
                                # Negative cell: take penalty or neutralize
                                # Option 1: take penalty
                                if prev_k == k:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i][j-1][prev_k] + coins[i][j])
                                # Option 2: neutralize (if we have budget)
                                if prev_k + 1 == k and k <= 2:
                                    dp[i][j][k] = max(dp[i][j][k], 
                                                    dp[i][j-1][prev_k])
        
        # Return the maximum among all neutralization states at destination
        return max(dp[m-1][n-1])