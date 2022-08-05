from typing import List
from collections import Counter


# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         countNums = Counter(nums)
#         res = self.permHelp(countNums)
#         return res
    
#     def permHelp(self, nums):
#         if len(nums) == 1:
#             key = list(nums.keys())[0]
#             if nums[key] == 1:
#                 return [[key]]
        
#         res = []
#         for num in nums.keys():
#             tmp_nums = nums.copy()
#             tmp_nums[num] -= 1
#             if tmp_nums[num] == 0:
#                 del tmp_nums[num]
#             for subset in self.permHelp(tmp_nums):
#                 res.append([num] + subset)

    

#         return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.help(nums)

    def help(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        i = 0
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            if i >= len(nums):
                return res
            for subset in self.help(nums[0:i] + nums[i + 1:]):
                res.append([nums[i]] + subset)
            i += 1

        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.permuteUnique([1, 2, 3]))
    print(s.permuteUnique([1,1,2]))
    # print(s.permuteUnique([3,3,0,3]))