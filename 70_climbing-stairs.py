class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        a = 1
        b = 1

        for i in range(1, n):
            t = b
            b += a
            a = t
        
        return b

if __name__ == "__main__":
    n = 5
    print(Solution().climbStairs(n))