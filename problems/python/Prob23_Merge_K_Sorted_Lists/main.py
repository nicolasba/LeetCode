# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists: List[ListNode]) -> ListNode:

    init_ll = ListNode()
    current_ll = init_ll

    while True:

        min_i = 0
        min_val = None

        for i, ll in enumerate(lists):
            if ll is not None:
                if min_val is None or ll.val < min_val:
                    min_i = i
                    min_val = ll.val

        if min_val is None:
            break;

        temp = ListNode(min_val, next=None)
        current_ll.next = temp
        current_ll = temp
        lists[min_i] = lists[min_i].next

    return init_ll.next


if __name__ == '__main__':
    mergeKLists('PyCharm')
