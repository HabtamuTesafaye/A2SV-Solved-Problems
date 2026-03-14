class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        pairs = 0
        result = 0
        
        for right in range(len(nums)):
            # Add nums[right]: it forms pairs with all previous occurrences
            if nums[right] in freq:
                pairs += freq[nums[right]]
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # Shrink from left while pairs >= k
            while pairs >= k:
                result += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] > 0:
                    # Remove pairs formed by nums[left]
                    pairs -= freq[nums[left]] 
                left += 1
        
        return result