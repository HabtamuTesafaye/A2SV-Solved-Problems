class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a ,b = 0 , 1
        count = 2
        while count <= n:
            a,b = b , a + b
            count += 1
        return b