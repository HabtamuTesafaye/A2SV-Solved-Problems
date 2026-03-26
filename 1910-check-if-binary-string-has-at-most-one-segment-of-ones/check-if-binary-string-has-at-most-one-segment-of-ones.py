class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segment_count = 0
        in_segment = False  # Flag to indicate if we are currently in a segment of '1's
        
        for char in s:
            if char == '1':
                if not in_segment:
                    # We found a new segment of '1's
                    segment_count += 1
                    in_segment = True
            else:
                in_segment = False  # Reset the flag when we encounter '0'
            
            # If we have more than one segment, we can return false early
            if segment_count > 1:
                return False
        
        return True  