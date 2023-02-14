from typing import List


# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         subarray_lens = []
#         cur_len = 0
#         start_i = 0
#         end_i = -1
#         for i, num in enumerate(nums):
#             if num == 1 and cur_len == 0:
#                 start_i = i
#                 end_i = i
#                 cur_len += 1
#             elif num == 1:
#                 cur_len += 1
#                 end_i += 1
#             elif cur_len != 0:
#                 subarray_lens.append((cur_len, start_i, end_i))
#                 cur_len = 0
#                 start_i = i + 1
#                 end_i = i

#         if cur_len != 0:
#             subarray_lens.append((cur_len, start_i, end_i))

#         if len(subarray_lens) == 0:
#             return 0

#         print(subarray_lens)

#         cur_max_len = subarray_lens[0][0]
#         cur_max_start_i = subarray_lens[0][1]
#         cur_max_end_i = subarray_lens[0][2]
#         cur_max_is_concatenation = False

#         if cur_max_len == len(nums):
#             return cur_max_len - 1

#         for i in range(len(subarray_lens) - 1):
#             first_sub_len = subarray_lens[i][0]
#             first_sub_start_i = subarray_lens[i][1]
#             first_sub_end_i = subarray_lens[i][2]

#             second_sub_len = subarray_lens[i + 1][0]
#             second_sub_start_i = subarray_lens[i + 1][1]
#             second_sub_end_i = subarray_lens[i + 1][2]

#             if second_sub_len > cur_max_len:
#                 cur_max_len = second_sub_len
#                 cur_max_start_i = second_sub_start_i
#                 cur_max_end_i = second_sub_end_i

#             if second_sub_start_i - first_sub_end_i == 2 and (first_sub_len + second_sub_len) > cur_max_len:
#                 cur_max_len = first_sub_len + second_sub_len

#         return cur_max_len

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        can_be_removed = 1
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                can_be_removed -= 1

            while (can_be_removed < 0):
                if (nums[i] == 0):
                    can_be_removed += 1
                i += 1

            result = max(result, j - i - (1 - can_be_removed) + 1 )
        
        if result == len(nums): 
            result -= 1
        
        return result





if __name__ == "__main__":
    # nums = [1,1,0,1]
    # nums = [1,1,0,0,1,1,1,0,1]
    # nums = [0,0,0]
    nums = [0,0,0,0,0]
    # nums = [1,1,1]
    # nums = [0,1,1,1,0,1,1,0,1]
    print(Solution().longestSubarray(nums))