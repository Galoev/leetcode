from typing import Optional
from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, None)
        cur_head = head

        while list1 and list2:
            if list1.val < list2.val:
                cur_head.next = ListNode(list1.val, None)
                cur_head = cur_head.next
                list1 = list1.next
            else:
                cur_head.next = ListNode(list2.val, None)
                cur_head = cur_head.next
                list2 = list2.next
        
        while list1:
            cur_head.next = ListNode(list1.val, None)
            cur_head = cur_head.next
            list1 = list1.next
        
        while list2:
            cur_head.next = ListNode(list2.val, None)
            cur_head = cur_head.next
            list2 = list2.next
        
        return head.next
       