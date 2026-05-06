class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: gravity — stones fall right
        for row in boxGrid:
            empty = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    empty = col - 1
                elif row[col] == '#':
                    row[col], row[empty] = row[empty], row[col]
                    empty -= 1
        
        # Step 2: rotate 90° CW → result is n x m
        result = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]
        
        return result