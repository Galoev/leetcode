from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev_sum = 0
        res = []
        for num in nums:
            prev_sum += num
            res.append(prev_sum)

        return res