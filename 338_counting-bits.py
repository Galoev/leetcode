from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(1, n+1):
            res[i] = res[i >> 1] + i%2

        return res

# class Solution:
#     def numToBin(self, num: int )-> List[int]:
#         res = []
#         while num > 1:
#             new_num = num // 2
#             res.append(num - (new_num * 2))
#             num = new_num
#         res.append(num)
#         return res

#     def __countBits(self, bits: List[int]) -> int:
#         res = 0
#         for bit in bits:
#             if bit == 1:
#                 res += 1

#         return res

#     def countBits(self, n: int) -> List[int]:
#         res = []
#         for i in range(n + 1):
#             bits = self.numToBin(i)
#             res.append(self.__countBits(bits))
#         return res


if __name__ == "__main__":
   print(Solution().countBits(5)) 
