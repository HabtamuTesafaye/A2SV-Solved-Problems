class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow edge case
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        while a >= b:
            temp = b
            multiple = 1

            # Double temp until it exceeds a
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            quotient += multiple

        return -quotient if negative else quotient