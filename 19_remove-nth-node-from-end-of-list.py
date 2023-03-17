from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        prev_slow = None
        slow = head
        fast = head
        for _ in range(n - 1):
            if fast.next:
                fast = fast.next

        while fast.next:
            fast = fast.next
            prev_slow = slow
            slow = slow.next
        
        if not prev_slow:
            return slow.next
        prev_slow.next = slow.next

        return head