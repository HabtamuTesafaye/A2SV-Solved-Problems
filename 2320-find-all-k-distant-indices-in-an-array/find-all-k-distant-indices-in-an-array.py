class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        result = []
        marked = [False] * n
        
        for j in range(n):
            if nums[j] == key:
                left = max(0, j - k)
                right = min(n - 1, j + k)
                
                for i in range(left, right + 1):
                    marked[i] = True
        
        for i in range(n):
            if marked[i]:
                result.append(i)
        
        return result