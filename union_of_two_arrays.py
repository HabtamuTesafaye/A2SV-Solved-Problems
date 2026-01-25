class Solution:    
    def findUnion(self, a, b):
        union = set(a)
        for x in b:
            union.add(x)
        return  union 
