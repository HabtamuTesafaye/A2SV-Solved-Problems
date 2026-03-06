class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captured = 0
        last_fort = -1  # Position of last 1 or -1
        
        for i in range(len(forts)):
            if forts[i] != 0:
                # We found a 1 or -1
                if last_fort != -1 and forts[i] != forts[last_fort]:
                    # Different types (1 and -1), so we can move between them
                    max_captured = max(max_captured, i - last_fort - 1)
                
                last_fort = i
        
        return max_captured