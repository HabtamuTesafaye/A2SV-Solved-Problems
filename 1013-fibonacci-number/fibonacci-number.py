class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a = n - 1
        b = n - 2
        return self.fib(a) + self.fib(b)