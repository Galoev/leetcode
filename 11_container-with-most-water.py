from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, min(height[l], height[r]) * (r - l))


        return max_area


if __name__ == "__main__":
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))
        
