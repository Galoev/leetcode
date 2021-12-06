class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        n1 = 1
        n2 = 2

        for i in range(3, n):
            n1, n2 = n2, n1 + n2

        return n2

# Это числа Фибоначи
# До Nой ступени можно добраться с N-1 и с N-2, надо суммировать сколькими способами можем попасть на N-1 и на N-2 и это ответ для N

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 0:
#             return 0
        
#         if n == 0:
#             return 1

#         n1 = self.climbStairs(n-1)
#         n2 = self.climbStairs(n-2)
        
#         return n1 + n2