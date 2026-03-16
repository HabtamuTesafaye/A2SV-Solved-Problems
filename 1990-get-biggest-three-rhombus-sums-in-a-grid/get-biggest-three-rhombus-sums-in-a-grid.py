class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        sums = set()
        
        for r in range(m):
            for c in range(n):
                
                sums.add(grid[r][c])  # radius 0
                
                max_k = min(r, m-1-r, c, n-1-c)
                
                for k in range(1, max_k+1):
                    total = 0
                    
                    x, y = r-k, c
                    
                    # top -> right
                    for _ in range(k):
                        total += grid[x][y]
                        x += 1
                        y += 1
                    
                    # right -> bottom
                    for _ in range(k):
                        total += grid[x][y]
                        x += 1
                        y -= 1
                    
                    # bottom -> left
                    for _ in range(k):
                        total += grid[x][y]
                        x -= 1
                        y -= 1
                    
                    # left -> top
                    for _ in range(k):
                        total += grid[x][y]
                        x -= 1
                        y += 1
                    
                    sums.add(total)
        
        return sorted(sums, reverse=True)[:3]