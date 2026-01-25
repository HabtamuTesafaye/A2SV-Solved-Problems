class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            covered = False
            for start , end in ranges:
                if start <= i and i <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True 
