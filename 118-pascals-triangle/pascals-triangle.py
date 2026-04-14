class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for  i in range(1, numRows):
            prev = triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(prev[j - 1] + prev[j])
            
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle
