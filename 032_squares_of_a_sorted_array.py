from typing import List
from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res_nums = deque()
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res_nums.appendleft(nums[left]**2)
                left += 1
            else:
                res_nums.appendleft(nums[right]**2)
                right -=1
        
        return list(res_nums)

    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     if nums[0] >= 0:
    #         return [x**2 for x in nums]

    #     pos_idx = self.findPosIdx(nums)
    #     if pos_idx == len(nums):
    #         return [nums[i]**2 for i in range(len(nums) - 1, -1, -1)]

    #     res_nums = [x**2 for x in nums[pos_idx:]]

    #     for num in nums[:pos_idx]:
    #         num = num**2
    #         self.insertNum(res_nums, num)

    #     return res_nums


    # def findPosIdx(self, nums: List[int]):
    #     for i, num in enumerate(nums):
    #         if num>=0:
    #             return i
    #     return len(nums)

    # def insertNum(self, nums: List[int], num: int):
    #     left = 0
    #     right = len(nums) - 1

    #     while left <= right:
    #         midle = left + (right - left) // 2
    #         if nums[midle] < num:
    #             left = midle + 1
    #         else:
    #             right = midle - 1
    #     nums.insert(left, num)
        
if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-7,-3,2,3,11]))
    print(s.sortedSquares([-1]))
    print(s.sortedSquares([-7,-4,-3,-1]))