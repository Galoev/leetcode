from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur_node = ListNode(head.val)
        new_head = ListNode(head.val)
        
        iter_node = head
        while iter_node.next:
            iter_node = iter_node.next

            cur_node = new_head
            new_head = ListNode(iter_node.val, cur_node)
        
        return new_head

def get_linked_list(vals):
    head = ListNode(vals[0])
    cur_head = head
    for i in range(1, len(vals)):
        cur_head.next = ListNode(vals[i])
        cur_head = cur_head.next
    return head

def print_linked_list(head: ListNode):
    while head:
        print(str(head.val) + " ", end='')
        head = head.next
    print()

s = Solution()
head = s.reverseList(get_linked_list([1, 2, 3, 4, 5]))
print_linked_list(head)