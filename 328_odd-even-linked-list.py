from typing import Optional
from utils import creat_linked_list
from utils import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
        
    #     odd_head = head
    #     even_head = ListNode(0, None)

    #     cur_odd = odd_head
    #     cur_even = even_head

    #     while cur_odd.next and cur_odd.next.next:
    #         prev = cur_odd.next 
    #         cur_odd.next = cur_odd.next.next
    #         cur_odd = cur_odd.next
    #         cur_even.next = prev
    #         cur_even = cur_even.next
        
    #     if cur_odd.next:
    #         cur_even.next = cur_odd.next
    #     else:
    #         cur_even.next = None
        
    #     cur_odd.next = even_head.next

    #     return odd_head


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = creat_linked_list(nums)
    print(Solution().oddEvenList(head))