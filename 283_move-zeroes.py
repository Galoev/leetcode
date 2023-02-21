from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1

            r +=1 



if __name__ == "__main__":
    s = Solution()
    nums = [0,1,0,3,12]
    nums = [1, 0]
    s.moveZeroes(nums)
    print(nums)
