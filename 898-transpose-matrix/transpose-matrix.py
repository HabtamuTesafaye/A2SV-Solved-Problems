class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        # create a mtarix intilzed to 0 based ont he row and cols size
        transpose  = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                transpose[col][row] = matrix[row][col]

        return transpose