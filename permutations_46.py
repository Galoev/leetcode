from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            for subset in self.permute(nums[0:i] + nums[i+1:]):
                res.append([nums[i]] + subset)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))