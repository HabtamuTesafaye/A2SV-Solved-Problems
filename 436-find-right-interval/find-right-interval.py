class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # Step 1: store (start, index)
        start_map = []

        for i in range(n):
            start = intervals[i][0]
            start_map.append((start, i))

        start_map.sort()    
            
        # Step 2: extract sorted starts
        starts = [s for s, _ in start_map]
        
        res = [-1] * n
        
        # Step 3: process each interval
        for i, (start, end) in enumerate(intervals):
            idx = bisect_left(starts, end)
            
            if idx < n:
                res[i] = start_map[idx][1]
        
        return res