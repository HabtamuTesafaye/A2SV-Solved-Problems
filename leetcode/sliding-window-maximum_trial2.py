class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        qeue = deque() 
        res = []

        for i, val in enumerate(nums):
            # evict out-of-window index
            if qeue and qeue[0] < i - k + 1:
                qeue.popleft()

            # maintain decreasing order — pop smaller values from back
            while qeue and nums[qeue[-1]] < val:
                qeue.pop()

            qeue.append(i)

            if i >= k - 1:
                res.append(nums[qeue[0]])

        return res