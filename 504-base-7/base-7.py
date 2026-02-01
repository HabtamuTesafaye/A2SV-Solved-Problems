class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        base7_digits = []
        
        while num > 0:
            remainder = num % 7
            base7_digits.append(str(remainder))
            num //= 7  
        
        if negative:
            base7_digits.append('-')
        
        # The digits are collected in reverse order, so reverse them
        base7_digits.reverse()
        
        return ''.join(base7_digits)