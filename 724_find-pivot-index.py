from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftPrefixSum = []
        prev_sum = 0
        for num in nums:
            prev_sum += num
            leftPrefixSum.append(prev_sum)
        
        rightPrefixSum = []
        prev_sum = 0
        for num in reversed(nums):
            prev_sum += num
            rightPrefixSum.append(prev_sum)
        rightPrefixSum = rightPrefixSum[::-1]
        rightPrefixSum.append(0)

        if rightPrefixSum[1] == 0:
            return 0

        for i in range(1, len(nums) - 1):
            if leftPrefixSum[i - 1] == rightPrefixSum[i + 1]:
                return i
        
        if leftPrefixSum[-2] == 0:
            return len(nums) - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [1,7,3,6,5,6]
    print(s.pivotIndex(nums))