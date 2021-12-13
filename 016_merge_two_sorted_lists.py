from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        result = merged

        while list1 and list2:
            if list1.val < list2.val:
                merged.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged.next = ListNode(list2.val) 
                list2 = list2.next

            merged = merged.next
        
        while list1:
            merged.next = ListNode(list1.val)
            list1 = list1.next
            merged = merged.next

        while list2:
            merged.next = ListNode(list2.val)
            list2 = list2.next
            merged = merged.next            

        return result.next

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not list1:
    #         return list2
    #     if not list2:
    #         return list1

    #     result = ListNode()
    #     iter = result

    #     while list1 or list2:
    #         if list1 and list2:
    #             if list1.val < list2.val:
    #                 iter.val = list1.val
    #                 list1 = list1.next
    #             else:
    #                 iter.val=list2.val
    #                 list2 = list2.next
    #             iter.next = ListNode()
    #             iter = iter.next
    #         elif list1:
    #             iter.val = list1.val
    #             if list1.next:
    #                 iter.next = list1.next
    #             break
    #         elif list2:
    #             iter.val=list2.val
    #             if list2.next:
    #                 iter.next = list2.next
    #             break
    #         else:
    #             iter.next = None
        
    #     return result


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
head = s.mergeTwoLists(get_linked_list([1, 2, 4]), get_linked_list([1, 3, 4]))
print_linked_list(head)