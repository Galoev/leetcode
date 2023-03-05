from typing import Optional
from utils import ListNode, creat_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        visited = {head}
        cur_head = head.next
        
        while cur_head:
            if cur_head in visited:
                return cur_head
            visited.add(cur_head)
            cur_head = cur_head.next
        
        return
    

if __name__ == "__main__":
    head = [3,2,0,-4]
    root = creat_linked_list(head)
    print(Solution().detectCycle(root))