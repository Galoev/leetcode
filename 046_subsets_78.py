from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for v in nums:
            cur_size = len(res)
            for i in range(cur_size):
                subset = res[i].copy()
                subset.append(v)
                res.append(subset.copy())

        return res

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         subset = []
#
#         def dfs(i):
#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return
#
#             subset.append(nums[i])
#             dfs(i + 1)
#
#             subset.pop()
#             dfs(i + 1)
#         dfs(0)
#         return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
