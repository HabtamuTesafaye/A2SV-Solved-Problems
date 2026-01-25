from collections import Counter

class Solution:
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        
        for key in count_b:
            if count_b[key] > count_a.get(key, 0):
                return False
        return True
