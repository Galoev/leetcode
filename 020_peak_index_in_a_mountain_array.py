from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            midle = left + (right - left) // 2
            if arr[midle] < arr[midle + 1]:
                left = midle + 1
            else:
                right = midle - 1
            
        return left
        
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     idx = 0
    #     while arr[idx] < arr[idx+1]:
    #         idx += 1
        
    #     return idx

s = Solution()
print(s.peakIndexInMountainArray([0,10,5,2]))
print(s.peakIndexInMountainArray([3,4,5,1]))