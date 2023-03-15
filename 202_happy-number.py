class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = self.numDigitSquareSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True
    
    def numDigitSquareSum(self, num: int) -> int:
        res = 0
        while num > 0:
            n = num % 10
            res = res + n**2
            num = num // 10
        
        return res
    

if __name__ == "__main__":
    print(Solution().isHappy(2))