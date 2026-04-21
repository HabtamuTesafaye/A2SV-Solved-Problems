class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # minium weight needed and the max we can carry 
         left , right = max(weights), sum(weights)
         while left < right:
            mid = (left + right ) // 2
            days_needed = 1
            curr_load = 0
            for w in weights:
                # ship the current if it is tooo many to load esle keep loading 
                if curr_load + w > mid:
                    days_needed += 1
                    curr_load = w
                else:
                    curr_load += w
            # if the days needed statisy can we find a smaller size else we need higher capacity
            if days_needed <= days:
                right = mid
            else:
                left = mid + 1
                
         return left
