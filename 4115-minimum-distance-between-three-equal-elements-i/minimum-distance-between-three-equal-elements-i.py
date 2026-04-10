class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        
        for idx, val in enumerate(nums):
            positions[val].append(idx)
        
        min_dist = float('inf')
        
        for indices in positions.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                i_, j_, k_ = indices[i], indices[i+1], indices[i+2]
                dist = 2 * (k_ - i_)
                min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1