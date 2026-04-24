class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:     
        def compute_sum(divisor: int) -> int:
            return sum((x + divisor - 1) // divisor for x in nums)

        left, right = 1, max(nums)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            total = compute_sum(mid)

            if total <= threshold:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer