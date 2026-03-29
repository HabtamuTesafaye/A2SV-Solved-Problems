class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        unique_set = set(nums)
        
        # Convert to sorted list for better range queries
        unique_list = sorted(unique_set)
        
        max_kept = 0
        
        # Use sliding window on sorted unique elements
        left = 0
        for right in range(len(unique_list)):
            # Shrink window from left until it's valid
            while unique_list[right] - unique_list[left] >= n:
                left += 1
            
            # Count elements in current window
            window_size = right - left + 1
            max_kept = max(max_kept, window_size)
        
        return n - max_kept