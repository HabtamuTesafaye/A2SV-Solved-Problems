class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            # Base cases
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                return i == len(s)
            
            # Check if first character matches
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: skip "x*" | Option 2: use '*' for one+ matches
                result = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Regular character match
                result = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dp(0, 0)