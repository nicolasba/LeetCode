from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = ListNode()
        curr = head

        if head:
            next = curr.next

            while next:
                if curr. val != next.val:
                    curr = next
                    next = next.next
                else:
                    curr.next = next.next
                    next = next.next

        ret.next = head

        return ret.next