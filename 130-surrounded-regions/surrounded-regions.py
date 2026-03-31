class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
    
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Check for boundary conditions
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            # Mark the cell as 'T'
            board[r][c] = 'T'
            # Explore all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Step 1: Mark all 'O's connected to the border
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == 'O':
                    dfs(r, c)
        
        # Step 2: Capture surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Capture the surrounded region
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  
            