class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001

        for num in arr1:
            counts[num] += 1
        
        result = []

        # add element in relative order of array 2 
        for num in arr2:
            while counts[num] > 0:
                result.append(num)
                counts[num] -= 1
                
        # add the reamingng elements 
        for i in range(len(counts)):
            while counts[i] > 0:
                result.append(i)
                counts[i] -= 1
        return result