class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrom(char) -> bool:
            left, right = 0, len(char) - 1
            while left <= right:
                if char[left] != char[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return ispalindrom(s[left + 1:right + 1]) or ispalindrom(s[left:right])
            left += 1
            right -= 1


        return True
