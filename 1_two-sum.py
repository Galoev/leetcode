from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in d:
                return [i, d[num]]
            d[target - num] = i


if __name__ == "__main__":
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))