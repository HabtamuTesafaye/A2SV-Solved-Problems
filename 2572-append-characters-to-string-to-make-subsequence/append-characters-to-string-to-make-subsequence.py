class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i , j = 0, 0
        n , m = len(s), len(t)

        while i < n and j < m:
            # find the common char and increment to get the chars to add to s from t 
            if s[i] == t[j]:
                j += 1
                
            i += 1

        return m - j