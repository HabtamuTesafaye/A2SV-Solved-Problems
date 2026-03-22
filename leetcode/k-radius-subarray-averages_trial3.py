class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        window = 2 * k + 1
        if window > n:
            return res
        
        # prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            res[i] = total // window
        
        return res