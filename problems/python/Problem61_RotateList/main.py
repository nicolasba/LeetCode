# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        list_size = 1
        tmp = head

        while tmp.next is not None:
            list_size += 1
            tmp = tmp.next

        tail = tmp

        tmp = head
        rem = k % list_size
        if rem > 0:
            for _ in range(list_size - rem - 1):
                tmp = tmp.next
        
            tail.next = head
            head = tmp.next 
            tmp.next = None

        return head