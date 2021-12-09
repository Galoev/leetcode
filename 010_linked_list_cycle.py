# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        
        return False



# from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return False
        
#         next_node = head
#         next_node.visited = True

#         while next_node.next:
#             if hasattr(next_node.next, 'visited'):
#                 return True
            
#             next_node = next_node.next
        
#         return False


# def get_linked_list(vals):
#     head = ListNode(vals[0])
#     cur_head = head
#     for i in range(1, len(vals)):
#         cur_head.next = ListNode(vals[i])
#         cur_head = cur_head.next
#     cur_head.next = head
#     return head

# s = Solution()

# print(s.hasCycle(get_linked_list([3,2,0,-4])))