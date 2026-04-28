class Solution:
    def arrangeCoins(self, n: int) -> int:
        left , right = 0, n
        while left <= right:
            mid = (left + right) // 2
            count = mid * (mid + 1) // 2

            if count == n:
                return mid
            elif count < n :
                left = mid + 1
            else:
                right = mid - 1
                
        return right