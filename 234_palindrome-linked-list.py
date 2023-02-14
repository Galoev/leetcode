# Definition for singly-linked list.
from typing import Optional
from utils import ListNode, creat_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        cur_head = head
        previous = None

        while cur_head:
            next_nodex = cur_head.next
            cur_head.next = previous
            previous = cur_head
            cur_head = next_nodex
        
        return previous

    def findMiddleNode(self, head: Optional[ListNode]) -> ListNode:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle_node = self.findMiddleNode(head)
        second_half_head = middle_node.next
        reversed_second_half_head = self.reverseList(second_half_head)

        while reversed_second_half_head:
            if head.val != reversed_second_half_head.val:
                return False
            
            head = head.next
            reversed_second_half_head = reversed_second_half_head.next

        return True


if __name__ == "__main__":
    # nums = [1,2,2,1]
    # nums = [1,1,1,1]
    nums = [1,2]
    head = creat_linked_list(nums)
    print(Solution().isPalindrome(head))