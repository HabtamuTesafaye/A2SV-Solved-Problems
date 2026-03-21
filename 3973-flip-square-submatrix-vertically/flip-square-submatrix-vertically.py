class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            # Top row index in submatrix
            top = x + i
            # Bottom row index in submatrix
            bottom = x + k - 1 - i
            
            # Swap the k elements in columns y to y+k-1
            for j in range(k):
                grid[top][y + j], grid[bottom][y + j] = grid[bottom][y + j], grid[top][y + j]
        
        return grid