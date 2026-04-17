class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        # Binary exponentiation
        result = 1.0
        current_power = x
        
        while n > 0:
            # If n is odd, multiply result by current power
            if n % 2 == 1:
                result *= current_power
            
            # Square the current power and halve the exponent
            current_power *= current_power
            n //= 2
        
        return result