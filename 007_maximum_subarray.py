class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            cur_sum = max(cur_sum + num, num)
            max_sum = max(cur_sum, max_sum)

        return max_sum


# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         for cur_sub_array_size in range(1, len(nums) + 1):
#             for start_idx in range(len(nums)):
#                 if (start_idx + cur_sub_array_size) > len(nums):
#                     break
#                 cur_sum = sum(nums[start_idx:(start_idx+cur_sub_array_size)])
#                 if cur_sum > max_sum:
#                     max_sum = cur_sum
#         return max_sum