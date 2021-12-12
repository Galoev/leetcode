from typing import Optional
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = None
        iter = head

        while iter:
            nxt = iter.next
            iter.next = new_head
            new_head = iter
            iter = nxt
        
        return new_head
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        if not fast.next:
            return slow
        
        return slow.next
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        midle_head = self.middleNode(head)
        reversed_midle_head = self.reverseList(midle_head)

        while reversed_midle_head:
            if head.val != reversed_midle_head.val:
                return False

            head = head.next
            reversed_midle_head = reversed_midle_head.next
        
        return True