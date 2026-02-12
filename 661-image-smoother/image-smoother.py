class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols =  len(img), len(img[0])

        result = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                total_sum = 0
                count = 0

                # findd the neigboure
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if 0 <= i < rows and 0 <= j < cols:
                            total_sum += img[i][j]
                            count += 1
                
                result[row][col] = total_sum // count

        return result