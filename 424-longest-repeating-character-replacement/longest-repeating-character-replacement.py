class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        ans = 0

        for right in range(len(s)):
            # get the current window maximum charcter
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # need to check if we need to shrink the current window so that it is ledd tham k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans 
