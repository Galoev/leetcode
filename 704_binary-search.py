from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            i = l + (r - l) // 2
            if nums[i] == target:
                return i
            elif r - l <= 0:
                return -1
            elif nums[i] > target:
                r = i - 1 
            else:
                l = i + 1


if __name__ == "__main__":
    # nums = [5]
    # target = 5
    # nums = [-1,0,3,5,9,12]
    # target = 9
    nums = [2,5]
    target = 5
    print(Solution().search(nums, target))