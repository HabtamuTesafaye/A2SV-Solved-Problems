class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        left , right = 0, len(matrix[0]) - 1
        top , bottom = 0 , len(matrix) - 1
        while top <= bottom and left <= right:
            #traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            #traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                #traverse from right to left
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                #traverse from bottom to top
                for i in range(bottom, top -1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
