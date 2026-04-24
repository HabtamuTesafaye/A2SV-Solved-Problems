class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # (start, original index)
        starts = sorted((intervals[i][0], i) for i in range(n))
        
        sorted_starts = [s for s, _ in starts]
        index_map = [idx for _, idx in starts]
        
        result = [-1] * n
        
        for i in range(n):
            end = intervals[i][1]
            
            pos = bisect.bisect_left(sorted_starts, end)
            
            if pos < n:
                result[i] = index_map[pos]
            else:
                result[i] = -1
        
        return result