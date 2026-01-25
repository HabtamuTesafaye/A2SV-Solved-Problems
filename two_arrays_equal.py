class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
            
        arr1 = sorted(a)
        arr2 = sorted(b)
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

#  simple line 
class Solution:
    def checkEqual(self, a, b) -> bool:
        return sorted(a) == sorted(b)
