class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
    
        def backtrack(current):
            # If we already found k strings, stop early
            if len(result) == k:
                return
            
            # Base case: string is complete
            if len(current) == n:
                result.append(current)
                return
            
            # Try each character in lexicographical order
            for char in ['a', 'b', 'c']:
                # Only add if different from last character
                if not current or current[-1] != char:
                    backtrack(current + char)
        
        backtrack("")
        return result[k - 1] if len(result) == k else ""