class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        result = []
        
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:  # char == 'D'
                result.append(high)
                high -= 1
        
        # Append the remaining number
        result.append(low)
        return result