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
        chars = list(s)
        deleted = 0
        while left <= right:
            if chars[left] != chars[right]:
                return ispalindrom(chars[left + 1:right + 1]) or ispalindrom(chars[left:right])
            left += 1
            right -= 1


        return True
