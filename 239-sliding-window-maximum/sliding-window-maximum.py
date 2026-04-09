class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() 
        res = []

        for i, val in enumerate(nums):
            # evict out-of-window index
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # maintain decreasing order — pop smaller values from back
            while dq and nums[dq[-1]] < val:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res