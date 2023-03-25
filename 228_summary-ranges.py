from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start_num = nums[0]
        cur_num = start_num
        i = 0
        while i < len(nums):
            start_num = nums[i]
            cur_num = start_num

            while i + 1 < len(nums) and (cur_num + 1) == nums[i + 1]:
                cur_num += 1
                i += 1
                continue

            if start_num == cur_num:
                res.append(str(start_num))
            else:
                res.append(f"{start_num}->{cur_num}")
            
            i += 1

        
        # if len(nums) > 2 and nums[-1] != nums[-2]:
        #     res.append(str(nums[-1]))
        
        return res
    

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))

        

            


