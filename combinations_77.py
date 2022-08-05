from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            if len(comb) == k: 
                res.append(comb.copy()) 
                return 
            for i in range(start, n+1):
                comb.append(i) 
                backtrack(i+1, comb) 
                comb.pop() 
        backtrack(1, [])

        return res

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         nums = list(range(1, n + 1))
#         print(nums)
#         return self.helpCombine(nums, k)

#     def helpCombine(self, nums: List[int], k: int) -> List[List[int]]:
#         if k == 1:
#             return [[x] for x in nums]
#         res = []

#         for i in range(len(nums)):
#             tmp_nums = nums[i+1:].copy()
#             for subset in self.helpCombine(tmp_nums, k - 1):
#                 res.append([nums[i]] + subset)

#         return res

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))