from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        init = True
        sorted_list, pointer = None, None

        while list1 and list2:

            if init:
                sorted_list = pointer = ListNode()
                init = False
            else:
                pointer.next = ListNode()
                pointer = pointer.next

            if list1.val < list2. val:
                pointer.val = list1.val
                list1 = list1.next
            else:
                pointer.val = list2.val
                list2 = list2.next

        if list1:
            if not sorted_list:
                sorted_list = list1
            else:
                pointer.next = list1

        if list2:
            if not sorted_list:
                sorted_list = list2
            else:
                pointer.next = list2

        return sorted_list
        