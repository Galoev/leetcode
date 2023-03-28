from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        res = 0
        for num in nums:
            s += num
            if (s-k) in d:
                res += d[s - k]
            
            d[s] = d.get(s, 0) + 1
        
        return res
