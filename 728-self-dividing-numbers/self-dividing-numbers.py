class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for n in range(left, right + 1):
            temp = n
            is_self_dividing = True

            while temp > 0:
                digit = temp % 10
                if digit == 0 or n % digit != 0:
                    is_self_dividing = False
                    break
                temp //= 10

            if is_self_dividing:
                result.append(n)

        return result