class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                dist1 = i
                break
        
        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                dist2 = n - 1 - i
                break
        
        return max(dist1, dist2)