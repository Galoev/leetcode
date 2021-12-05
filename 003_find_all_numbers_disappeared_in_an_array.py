class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        all_nums = set(range(1, len(nums) + 1))
        return list(all_nums - unique_nums)