from typing import Optional
from utils import ListNode
from utils import creat_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head: ListNode):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge(self, left: ListNode, right: ListNode):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next 
        
        if left:
            tail.next = left
        
        if right:
            tail.next = right

        return dummy.next


if __name__ == "__main__":
    head = [4,2,1,3]
    root = creat_linked_list(head)
    print(Solution().sortList(root))