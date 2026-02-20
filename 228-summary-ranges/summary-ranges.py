class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        if n == 0:
            return res
        
        start = nums[0]
        prev = nums[0]
        
        for i in range(1, n):
            if nums[i] == prev + 1:
                prev = nums[i]
            else:
                if start == prev:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{prev}")
                start = nums[i]
                prev = nums[i]
        
        # add the last range
        if start == prev:
            res.append(str(start))
        else:
            res.append(f"{start}->{prev}")
        
        return res