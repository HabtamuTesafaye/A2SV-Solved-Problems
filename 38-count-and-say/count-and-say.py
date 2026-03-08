class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        
        # Build the sequence iteratively from position 1 to n
        for _ in range(n - 1):
            current = self._rle_encode(current)
        
        return current
    
    def _rle_encode(self, s: str) -> str:
        """Apply run-length encoding to the string."""
        result = []
        i = 0
        
        while i < len(s):
            digit = s[i]
            count = 1
            
            # Count consecutive identical digits
            while i + count < len(s) and s[i + count] == digit:
                count += 1
            
            # Append count and digit
            result.append(str(count) + digit)
            i += count
        
        return "".join(result)