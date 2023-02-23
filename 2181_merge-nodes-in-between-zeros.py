from utils import ListNode
from utils import creat_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_sum = 0
        root = ListNode(0, None)
        cur_root = root
        while head.next:
            head = head.next
            if head.val == 0:
                cur_root.next = ListNode(cur_sum, None)
                cur_root = cur_root.next
                cur_sum = 0
                continue
            cur_sum += head.val
        return root.next


if __name__ == "__main__":
    s = Solution()
    # head = [0,3,1,0,4,5,2,0]
    head = [0,1,0,3,0,2,2,0]
    root = creat_linked_list(head)
    print(s.mergeNodes(root))
