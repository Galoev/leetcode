from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_index = self.__countZeros(nums)
        if len(zeros_index) > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        mult = 1

        for n in nums:
            if n != 0:
                mult *= n

        if len(zeros_index) == 1:
            res[zeros_index[0]] = mult
            return res

        for i, n in enumerate(nums):
            res[i] = int(mult / n)
        
        return res

        
    def __countZeros(self, nums: List[int]) -> List[int]:
        res = []

        for i, n in enumerate(nums):
            if n == 0:
                res.append(i)

        return res


if __name__ == "__main__":
    s = Solution()
    # nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    print(s.productExceptSelf(nums))