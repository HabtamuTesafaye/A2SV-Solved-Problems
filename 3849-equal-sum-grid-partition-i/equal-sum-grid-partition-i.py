class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        # If total is odd, cannot split equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Try horizontal cuts
        running_sum = 0
        for i in range(m - 1):  # ensure bottom part non-empty
            running_sum += sum(grid[i])
            if running_sum == target:
                return True
        
        # Compute column sums
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        
        # Try vertical cuts
        running_sum = 0
        for j in range(n - 1):  # ensure right part non-empty
            running_sum += col_sums[j]
            if running_sum == target:
                return True
        
        return False