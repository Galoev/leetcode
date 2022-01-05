from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findDuplicate(slef, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        slow_2 = nums[0]
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        
        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([3,1,3,4,2]))
    print(s.findDuplicate([1,3,4,2,2]))