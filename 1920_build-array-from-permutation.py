from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans


if __name__ == "__main__":
    # nums = [0,2,1,5,3,4]
    nums = [5,0,1,2,3,4]
    print(Solution().buildArray(nums))