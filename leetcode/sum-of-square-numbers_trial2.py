class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(pow(c, 0.5)) + 1
        while a <= b:
            total = pow(a, 2) + pow(b, 2)
            if total == c:
                return True
            elif total < c:
                a += 1
            else:
                b -= 1
        return False