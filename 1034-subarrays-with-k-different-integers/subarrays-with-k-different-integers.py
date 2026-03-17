class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            count = defaultdict(int)
            distinct = 0
            result = 0
            left = 0
            
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    distinct += 1
                count[nums[right]] += 1
                
                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                
                result += right - left + 1  
            
            return result
        
        return atMost(k) - atMost(k - 1)