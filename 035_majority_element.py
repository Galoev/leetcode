from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = None
        vote = 0

        for num in nums:
            if vote == 0:
                result = num
            if num == result:
                vote += 1
            else:
                vote -= 1

        return result
    
    # def majorityElement(self, nums: List[int]) -> int:
    #     c = Counter(nums)
    #     return c.most_common(1)[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))