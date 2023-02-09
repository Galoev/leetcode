from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_n_nums = 0
        cur_sum = 0
        n = len(nums)
        for i in range(n):
            cur_sum += nums[i]
            sum_n_nums += i
        sum_n_nums += n
        return sum_n_nums - cur_sum


if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))