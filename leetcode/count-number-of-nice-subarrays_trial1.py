class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        prefix = 0
        ans = 0
        
        for num in nums:
            if num % 2 == 1:
                prefix += 1
            
            ans += count[prefix - k]
            count[prefix] += 1
        
        return ans