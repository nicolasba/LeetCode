# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return recSwap(head)
        
    
def recSwap(head):
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    tmp = second.next
    second.next = first
    first.next = recSwap(tmp)

    return second
        