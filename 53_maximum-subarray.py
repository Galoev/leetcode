from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(sum(nums), self.maxSubArray(nums[1:]))
