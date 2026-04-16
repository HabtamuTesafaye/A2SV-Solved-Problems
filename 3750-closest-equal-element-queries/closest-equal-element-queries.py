class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = []
        
        for q in queries:
            indices = pos[nums[q]]
            
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            i = bisect.bisect_left(indices, q)
            
            # circular neighbors using modulo
            left = indices[(i - 1) % len(indices)]
            right = indices[(i + 1) % len(indices)]
            
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            res = min(d1, n - d1, d2, n - d2)
            ans.append(res)
        
        return ans