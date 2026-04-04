class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText.rstrip()
        
        cols = len(encodedText) // rows
        result = []
        
        # For each starting column in row 0
        for start_col in range(cols):
            row = 0
            col = start_col
            
            # Follow diagonal down-right
            while row < rows and col < cols:
                # Calculate index in encodedText
                idx = row * cols + col
                result.append(encodedText[idx])
                row += 1
                col += 1
        
        return ''.join(result).rstrip()