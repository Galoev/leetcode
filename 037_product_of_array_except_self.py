from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        for i in range(len(nums) - 1):
            prefix_products.append(prefix_products[-1] * nums[i])
        
        sufix_products = [0 for _ in range(len(nums))]
        sufix_products[len(nums) - 1] = 1
        for i in range(len(nums) - 1, 0, -1):
            sufix_products[i - 1] = sufix_products[i] * nums[i]
        
        result = []
        for prefix, sufix in zip(prefix_products, sufix_products):
            result.append(prefix * sufix)
        
        return result


    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = 1
    #     zero_count = 0
    #     idx_first_zero = -1
    #     for i, num in enumerate(nums):
    #         if num == 0:
    #             zero_count += 1
    #             if zero_count > 1:
    #                 break
    #             else:
    #                 idx_first_zero = i
    #             continue
            
    #         product *= num
        
    #     if zero_count >= 2:
    #         return [0 for _ in range(len(nums))]
        
    #     if zero_count == 1:
    #         res = [0 for _ in range(len(nums))]
    #         res[idx_first_zero] = product
    #         return res
        
    #     res = []
    #     for num in nums:
    #         res.append(int(product/num))
    #     return res


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))
    print(s.productExceptSelf([-1,1,0,-3,3,0]))
