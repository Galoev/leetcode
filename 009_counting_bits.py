class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(1, n+1):
            res[i] = res[i >> 1] + i%2

        return res


# from typing import List

# class Solution:
#     def addOneBit(self, bit_num: List[int]) -> int:
#         count_bit = 0
#         add_coef = 1
#         for i in range(len(bit_num)):
#             if (bit_num[i] + add_coef) == 2:
#                 bit_num[i] = 0
#                 continue
#             bit_num[i] += add_coef
#             add_coef = 0
#             if (bit_num[i] == 1):
#                 count_bit += 1
#         if add_coef == 1:
#             count_bit += 1
#             bit_num.append(add_coef)
#         return count_bit, bit_num

#     def countBits(self, n: int) -> List[int]:
#         cur_bit_num = [0]
#         res = [0]
#         for i in range(1, n+1):
#             coutn_bit, cur_bit_num = self.addOneBit(cur_bit_num)
#             res.append(coutn_bit)
#         return res

# s = Solution()
# print(s.countBits(2))