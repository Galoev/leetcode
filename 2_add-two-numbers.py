from typing import Optional
from utils import ListNode, creat_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        val = l1.val + l2.val
        offset = val // 10
        head = ListNode(val % 10, None)
        cur_head = head

        l1 = l1.next
        l2 = l2.next

        while l1 != None or l2 != None:
            val1 = 0
            if l1 != None:
                val1 = l1.val
                l1 = l1.next

            val2 = 0
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            
            val = val1 + val2 + offset
            offset = val // 10

            cur_head.next = ListNode(val % 10, None)
            cur_head = cur_head.next

        if offset:
            cur_head.next = ListNode(offset, None)

        return head



if __name__ == "__main__":
    s = Solution()
    # l1 = creat_linked_list([2,4,3])
    # l2 = creat_linked_list([5,6,4])
    l1 = creat_linked_list([9,9,9,9,9,9,9])
    l2 = creat_linked_list([9,9,9,9])
    print(s.addTwoNumbers(l1, l2))