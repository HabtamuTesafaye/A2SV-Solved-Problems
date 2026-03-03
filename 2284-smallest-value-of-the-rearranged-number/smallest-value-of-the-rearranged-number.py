class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)

        # Negative case
        if s[0] == '-':
            digits = list(s[1:])
            digits.sort(reverse=True)
            return -int("".join(digits))

        # Positive case
        digits = list(s)
        digits.sort()

        # If all digits are zero (like "0", "00")
        if digits[-1] == '0':
            return 0

        i = 0
        while i < len(digits) and digits[i] == '0':
            i += 1

        first = digits[i]
        digits.pop(i)

        result = first + "".join(digits)
        return int(result)