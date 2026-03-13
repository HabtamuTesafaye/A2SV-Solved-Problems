class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        
        # first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        ans = count
        
        # slide window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            
            ans = max(ans, count)
        
        return ans