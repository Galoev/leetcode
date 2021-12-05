class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(range(len(nums) + 1))
        cur_sum = sum(nums)
        return total_sum - cur_sum