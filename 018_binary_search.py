from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            midle = left + (right - left) // 2
            if nums[midle] == target:
                return midle
            elif nums[midle] < target:
                left = midle + 1
            else:
                right = midle - 1
        
        return -1

s = Solution()
# print(s.search([-1,0,3,5,9,12], 9))

print(s.search([5], 5))