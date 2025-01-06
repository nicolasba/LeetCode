from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    count, mid_index = 0, 0
    temp = head

    while temp:
        count += 1
        temp = temp.next
    
    mid_index = int(count / 2)

    for _ in range(mid_index):
        head = head.next

    return head

if __name__ == '__main__':
    ll = ListNode(1,ListNode(2, ListNode(3, ListNode(4))))
    ml = middleNode(ll)

    while ml:
        print(ml.val)
        ml = ml.next
