from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            
            subset.pop()
            while (i + 1) < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        
        return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]

    #     for v in nums:
    #         cur_size = len(res)
    #         for i in range(cur_size):
    #             subset = res[i].copy()
    #             subset.append(v)
    #             if subset not in res:
    #                 res.append(subset.copy())

    #     return res
    
    


if __name__ == "__main__":
    s = Solution()
    # print(s.subsetsWithDup([1, 2, 2, 3]))
    print(s.subsetsWithDup([5, 5, 5, 5, 5]))