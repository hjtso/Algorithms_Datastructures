# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp_head = ListNode(None, None)
        while head:
            next = head.next
            head.next = tmp_head.next
            tmp_head.next = head
            head = next

        return tmp_head.next