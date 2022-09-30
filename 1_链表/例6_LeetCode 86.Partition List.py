# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = ListNode(0)
        more_head = ListNode(0)
        less_prt = less_head
        more_prt = more_head
        while head:
            if head.val < x:
                less_prt.next = head
                less_prt = head
            else:
                more_prt.next = head
                more_prt = head
            head = head.next

        less_prt.next = more_head.next
        more_prt.next = None
        return less_head.next
