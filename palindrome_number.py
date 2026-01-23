class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        right = len(num) - 1
        for left in range(len(num)):
            if left >= right:
                break
            if num[left] != num[right]:
                return False
            right -= 1
        return True
