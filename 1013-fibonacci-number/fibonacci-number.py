class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0

        a = n - 1
        b = n - 2
        return self.fib(a) + self.fib(b)