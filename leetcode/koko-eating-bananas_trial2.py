class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / k)
            return total_hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left