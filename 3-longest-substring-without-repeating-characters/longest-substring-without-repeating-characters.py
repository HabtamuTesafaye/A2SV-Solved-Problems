class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = Counter()
        max_len = 0
        left = 0
        for right in range(len(s)):
            ch = s[right]
            seen[ch] += 1
            while seen[ch] > 1:
                seen[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
        
        return max_len