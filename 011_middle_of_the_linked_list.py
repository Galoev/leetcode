from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
        

def get_linked_list(vals):
    head = ListNode(vals[0])
    cur_head = head
    for i in range(1, len(vals)):
        cur_head.next = ListNode(vals[i])
        cur_head = cur_head.next
    cur_head.next = head
    return head

s = Solution()

print(s.hasCycle(get_linked_list([3,2,0,-4])))