from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        current = result

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return result.next


    def removeElementsMy(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        slow = None
        fast = head
        
        while fast:
            if fast.val == val:
                if slow:                    
                    slow.next = fast.next
                    fast = fast.next
                else:
                    fast = fast.next
                    head = fast
                continue
            
            if slow:
                fast = fast.next
                slow = slow.next
            else:
                slow = fast
                fast = fast.next

        return head

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
head = s.removeElements(get_linked_list([1,2,6,3,4,5,6]), 6)
print_linked_list(head)

head = s.removeElements(get_linked_list([7,7,7,7]), 7)
print_linked_list(head)