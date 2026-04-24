class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        
        for h in houses:
            pos = bisect.bisect_left(heaters, h)
            
            # distance to right heater
            right_dist = float('inf')
            if pos < len(heaters):
                right_dist = abs(heaters[pos] - h)
            
            # distance to left heater
            left_dist = float('inf')
            if pos > 0:
                left_dist = abs(h - heaters[pos - 1])
            
            # best for this house
            ans = max(ans, min(left_dist, right_dist))
        
        return ans