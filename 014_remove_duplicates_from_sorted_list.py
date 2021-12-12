from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        result = ListNode(val=head.val-1)
        result.next = head

        slow = result
        fast = result.next
        prev_fast = fast

        while fast:
            if slow.val == fast.val:
                prev_fast = fast
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        
        if slow.val == prev_fast.val:
            slow.next = None

        return result.next