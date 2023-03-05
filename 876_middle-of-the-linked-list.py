from typing import Optional
from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head

        slow = head
        fast = head.next.next
        while fast:
            slow = slow.next
            if not fast.next or not fast.next.next:
                return slow
            fast = fast.next.next
        return slow