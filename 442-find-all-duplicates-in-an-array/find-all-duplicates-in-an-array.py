class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for x in nums:
            # Step 1: Use the absolute value (because it might have been flipped)
            # Subtract 1 to convert the number (1 to n) to an index (0 to n-1)
            index = abs(x) - 1
            
            # Step 2: Check the "signpost" at that index
            if nums[index] < 0:
                # If it's already negative, we found a duplicate!
                result.append(abs(x))
            else:
                # If it's positive, flip it to negative to "mark" it
                nums[index] = -nums[index]
                
        return result