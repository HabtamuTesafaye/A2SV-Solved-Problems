class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        quota = n // 4
        count = Counter(s)
        
        excess = sum(1 for c in "QWER" if count[c] > quota)
        
        if excess == 0:
            return 0
        
        result = n
        left = 0
        
        for right in range(n):
            rc = s[right]
            if count[rc] == quota + 1: 
                excess -= 1
            count[rc] -= 1
            
            while excess == 0:
                result = min(result, right - left + 1)
                lc = s[left]
                count[lc] += 1
                if count[lc] == quota + 1:  
                    excess += 1
                left += 1
        
        return result