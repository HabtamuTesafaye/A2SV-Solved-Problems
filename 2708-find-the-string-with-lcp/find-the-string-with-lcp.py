class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Validate diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
        
        # Build the string
        word = [''] * n
        current_char = 'a'
        
        for i in range(n):
            if word[i] == '':  # Not yet assigned
                if current_char > 'z':
                    return ""  # Ran out of letters
                
                word[i] = current_char
                
                # Assign to all positions where lcp[i][j] > 0
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = current_char
                
                current_char = chr(ord(current_char) + 1)
        
        # Verify using LCP properties
        for i in range(n):
            for j in range(n):
                if word[i] == word[j]:
                    # If characters match, lcp[i][j] should be 1 + lcp[i+1][j+1]
                    expected = lcp[i + 1][j + 1] + 1 if i + 1 < n and j + 1 < n else 1
                    if lcp[i][j] != expected:
                        return ""
                else:
                    # If characters differ, lcp[i][j] must be 0
                    if lcp[i][j] != 0:
                        return ""
        
        return ''.join(word)