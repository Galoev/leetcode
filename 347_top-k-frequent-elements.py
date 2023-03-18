from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        commmon = counter.most_common()
        res = []
        for t in commmon:
            k -= 1
            res.append(t[0])
            if k == 0:
                break

        return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    print(Solution().topKFrequent(nums, k))