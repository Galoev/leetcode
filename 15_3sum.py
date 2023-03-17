from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        while i < len(nums) and nums[i] <= 0:
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                i += 1
                continue
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                if (a + nums[l] + nums[r]) == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    continue
                if nums[l] + nums[r] > (-a):
                    r -= 1
                else:
                    l += 1
            i += 1
        
        return res


if __name__ == "__main__":
    print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
