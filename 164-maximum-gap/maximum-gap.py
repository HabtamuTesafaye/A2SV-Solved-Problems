from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        minVal = min(nums)
        maxVal = max(nums)
        
        if minVal == maxVal:
            return 0
        
        # Step 1: Compute bucket size
        bucket_size = max(1, (maxVal - minVal) // (n - 1))
        bucket_count = (maxVal - minVal) // bucket_size + 1
        
        # Step 2: Initialize buckets
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        
        # Step 3: Distribute numbers into buckets
        for num in nums:
            index = (num - minVal) // bucket_size
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
        
        # Step 4: Compute maximum gap
        max_gap = 0
        prev_max = minVal
        
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]
        
        return max_gap