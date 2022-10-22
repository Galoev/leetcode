from typing import List
from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count_nums = Counter(nums)
#         freq = [[] for i in range(len(nums) + 1)]
#         res = []

#         for num, count in count_nums.items():
#             freq[count].append(num)

#         i = len(nums)
#         while k > 0:
#             some_nums = freq[i]
#             for some_num in some_nums:
#                 res.append(some_num)
#                 k -= 1
#                 if k == 0:
#                     break
#             i -= 1

#         return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)

        res = []
        for i in range(k):
            cur_max_num = next(iter(count_nums))
            cur_max_count = count_nums[cur_max_num]
            for num, count in count_nums.items():
                if count > cur_max_count:
                    cur_max_num = num
                    cur_max_count = count
            count_nums.pop(cur_max_num)
            res.append(cur_max_num)
        
        return res


if __name__ == "__main__":
    s = Solution()
    # nums = [1,1,1,2,2,3]
    nums = [4,1,-1,2,-1,2,3]
    k = 2

    print(s.topKFrequent(nums, k))

