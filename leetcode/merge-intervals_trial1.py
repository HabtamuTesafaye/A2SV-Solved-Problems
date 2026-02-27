class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time (first element)
        intervals.sort()

        # Initialize merged list with the first interval
        merged = [intervals[0]]

        # For each interval starting from the second
        for current in intervals[1:]:
            prev = merged[-1]

            # If current interval overlaps with the previous interval
            if current[0] <= prev[1]:
                prev[1] = max(prev[1], current[1])
            # If no overlap, add current interval as a new interval
            else:
                merged.append(current)

        return merged