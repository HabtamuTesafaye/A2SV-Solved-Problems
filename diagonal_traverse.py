class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = {}
        m, n = len(mat), len(mat[0])
        
        #  Group elements by diagonal
        for i in range(m):
            for j in range(n):
                d = i + j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(mat[i][j])
        
        # # Step 2: Traverse the diagonals in order
        res = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                res.extend(diagonals[d][::-1])
            else:
                res.extend(diagonals[d])
        return res
