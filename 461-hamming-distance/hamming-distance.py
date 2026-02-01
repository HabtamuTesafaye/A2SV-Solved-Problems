class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        distance = 0
        while xor_result:
            distance += xor_result & 1
            xor_result >>= 1 
        return distance