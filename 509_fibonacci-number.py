class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for i in range(n - 2):
            tmp = b
            b = a + b
            a = tmp
        return b